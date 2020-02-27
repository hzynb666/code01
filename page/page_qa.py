import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 页面对象

# 对象库层
from page.page_my import MyProxy
from page.page_user_login import UserLoginProxy
from tool.utils import DriverUtil


class QaPage(BasePage):
    def __init__(self):
        super().__init__()
        self.bug = By.CSS_SELECTOR, '[data-id="bug"]'

    # bug 定位
    def find_bug(self):
        return self.base_find_element(self.bug)


# 操作层
class QaHandle(BaseHandle):
    def __init__(self):
        self.qa_page = QaPage()

    # bug 点击
    def click_bug(self):
        self.base_click_element(self.qa_page.find_bug())


# 业务层
class QaProxy:
    def __init__(self):
        self.qa_handle = QaHandle()

    # 进入 bug浏览页面
    def go_bug_browse(self):
        self.qa_handle.click_bug()



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

    # 退出浏览器
    time.sleep(2)
    DriverUtil.quit_driver()
