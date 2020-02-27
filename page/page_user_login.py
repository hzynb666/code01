# 页面对象
import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from tool.utils import DriverUtil


class UserLoginPage(BasePage):

    def __init__(self):
        super().__init__()
        # (定位策略,定位依据)
        self.ceshi_jia = (By.LINK_TEXT, "测试甲")
        self.login = (By.CSS_SELECTOR, "#submit")

    # 测试甲超链接
    def find_ceshi_jia(self):
        return self.base_find_element(self.ceshi_jia)

    # 登录按钮
    def find_login(self):
        return self.base_find_element(self.login)


# 操作层
class UserLoginHandle(BaseHandle):
    def __init__(self):
        self.user_login_page = UserLoginPage()

    # 测试甲点击
    def click_ceshi_jia(self):
        self.base_click_element(self.user_login_page.find_ceshi_jia())

    # 登录点击
    def click_login(self):
        self.base_click_element(self.user_login_page.find_login())


# 业务层
class UserLoginProxy:
    def __init__(self):
        self.user_login_handle = UserLoginHandle()

    # 测试登录
    def tester_login(self):
        # 点击测试甲
        self.user_login_handle.click_ceshi_jia()
        # 点击登录
        self.user_login_handle.click_login()


if __name__ == '__main__':
    # 打开浏览器
    driver = DriverUtil.get_driver()
    # 打开登录页面
    driver.get("http://demo.zentao.net/user-login.html")

    # 测试登录
    ulp = UserLoginProxy()
    ulp.tester_login()

    # 退出浏览器
    time.sleep(2)
    DriverUtil.quit_driver()
