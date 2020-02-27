import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 页面对象

# 对象库层
from page.page_user_login import UserLoginProxy
from tool.utils import DriverUtil


class MyPage(BasePage):
    def __init__(self):
        super().__init__()
        self.ceshi = By.CSS_SELECTOR, '[data-id="qa"]'

    # 测试超链接
    def find_ceshi(self):
        return  self.base_find_element(self.ceshi)


# 操作层
class MyHandle(BaseHandle):
    def __init__(self):
        self.my_page = MyPage()

    # 点击测试
    def click_ceshi(self):
        self.base_click_element(self.my_page.find_ceshi())


# 业务层
class MyProxy:
    def __init__(self):
        self.my_handle = MyHandle()

    # 进入质量管理页面QA
    def go_qa(self):
        self.my_handle.click_ceshi()


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

    # 退出浏览器
    time.sleep(2)
    DriverUtil.quit_driver()
