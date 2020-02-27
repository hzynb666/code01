import json
import logging
import time
import unittest

# 测试用例
from parameterized import parameterized

from config import BASE_PATH
from page.page_bug_browse import BugBrowseProxy
from page.page_bug_create import BugCreateProxy
from page.page_my import MyProxy
from page.page_qa import QaProxy
from page.page_user_login import UserLoginProxy
from tool.utils import DriverUtil, exists_text


# 读取测试数据 [(),(),()]
def get_case_data():
    # 创建存放数据列表
    result = list()

    # 读取数据构造数据元祖,放到列表中
    # a.读取json文件
    with open(BASE_PATH + "/data/create_bug.json", "r", encoding="utf-8") as f:
        python_data = json.load(f)
        # b.构造数据
        for data in python_data:
            bug_title = data.get("bug_title")
            expect = data.get("expect")
            result.append((bug_title, expect))
    # 返回存放数据列表
    return result


class TestTesterCreateBug(unittest.TestCase):
    driver = None

    # fixture -- 类级别  工具加载
    # 浏览器获取 -- 类级别 setup
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()
        cls.ulp = UserLoginProxy()
        cls.myp = MyProxy()
        cls.qp = QaProxy()
        cls.bbp = BugBrowseProxy()
        cls.bcp = BugCreateProxy()
        cls.driver.get("http://demo.zentao.net/user-login.html")
        # 1.用户登录
        cls.ulp.tester_login()

    # 浏览器销毁 -- 类级别 teardown
    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 方法级别 用例前置条件
    # 前置条件  打开用户登录界面
    def setUp(self):
        pass

    def tearDown(self):
        time.sleep(2)

    # 参数表示数据
    # 添加参数化工具
    # 传入参数数据
    @parameterized.expand(get_case_data())
    def test01_create_bug(self, bug_title, expect):
        # 测试用例业务
        logging.info("添加用例的标题是: {}".format(bug_title))
        # 2.进入测试页面
        self.myp.go_qa()
        # 3.进入Bug浏览页面
        self.qp.go_bug_browse()
        # 4.点击提Bug
        self.bbp.go_create_bug()
        # 5.点选影响版本(默认第一个)
        # 6.输入Bug标题
        # 7.点击保存
        time.sleep(3)
        self.bcp.create_bug(bug_title)
        # 用例执行结果断言
        # 判断页面中是否存在"保存成功"四个
        # 如果能定位到 -- 存在 -- 符合预期
        # 如果不能定位到 -- 不存在 -- 不符合预期
        result = exists_text(expect)
        self.assertTrue(result)
