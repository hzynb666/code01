import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 页面对象

# 对象库层
from page.page_my import MyProxy
from page.page_qa import QaProxy
from page.page_user_login import UserLoginProxy
from tool.utils import DriverUtil


class BugBrowsePage(BasePage):
    def __init__(self):
        super().__init__()
        self.ti_bug = By.CSS_SELECTOR, ".pull-right>.btn-primary"

    # 提Bug 超链接
    def find_ti_bug(self):
        return self.base_find_element(self.ti_bug)


# 操作层
class BugBrowseHandle(BaseHandle):
    def __init__(self):
        self.bbp = BugBrowsePage()

    # 提Bug  点击操作
    def click_ti_bug(self):
        self.base_click_element(self.bbp.find_ti_bug())


# 业务层
class BugBrowseProxy:
    def __init__(self):
        self.bbh = BugBrowseHandle()

    # 提Bug点击进入Bug创建页面
    def go_create_bug(self):
        self.bbh.click_ti_bug()


if __name__ == '__main__':
    # 打开浏览器
    driver = DriverUtil.get_driver()
    # 打开登录页面
    driver.get("http://demo.zentao.net/user-login.html")

    # 测试登录
    ulp = UserLoginProxy()
    ulp.tester_login()
    myp = MyProxy()
    myp.go_qa()
    qp = QaProxy()
    qp.go_bug_browse()
    bbp = BugBrowseProxy()
    bbp.go_create_bug()

    # 退出浏览器
    time.sleep(2)
    DriverUtil.quit_driver()
