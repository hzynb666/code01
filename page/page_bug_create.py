import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 页面对象

# 对象库层
from page.page_bug_browse import BugBrowseProxy
from page.page_my import MyProxy
from page.page_qa import QaProxy
from page.page_user_login import UserLoginProxy
from tool.utils import DriverUtil


class BugCreatePage(BasePage):
    def __init__(self):
        super().__init__()
        self.opened_build = By.CSS_SELECTOR, "#openedBuild_chosen"
        self.build = By.CSS_SELECTOR, '#openedBuild_chosen [data-option-array-index="0"]'
        self.bug_title = By.CSS_SELECTOR, '#title'
        self.submit = By.CSS_SELECTOR, '#submit'

    # opened_build
    def find_opened_build(self):
        return self.base_find_element(self.opened_build)

    # build
    def find_buile(self):
        return self.base_find_element(self.build)

    # bug_title
    def find_bug_title(self):
        return self.base_find_element(self.bug_title)

    # submit
    def find_submit(self):
        return self.base_find_element(self.submit)


# 操作层
class BugCreateHandle(BaseHandle):
    def __init__(self):
        self.bcp = BugCreatePage()

    # opened_build -- click
    def click_opened_build(self):
        self.base_click_element(self.bcp.find_opened_build())

    # build  -- click
    def click_build(self):
        self.base_click_element(self.bcp.find_buile())

    # bug_title  -- input
    def input_bug_title(self, title):
        self.base_input_text(self.bcp.find_bug_title(), title)

    # submit -- click
    def click_submit(self):
        self.base_click_element(self.bcp.find_submit())


# 业务层
class BugCreateProxy:
    def __init__(self):
        self.bch = BugCreateHandle()

    # 创建缺陷 create_bug
    def create_bug(self, title):
        # opened_build -- click
        self.bch.click_opened_build()
        # build  -- click
        self.bch.click_build()
        # bug_title  -- input
        self.bch.input_bug_title(title)
        # submit -- click
        # 滚动滚动条
        DriverUtil.get_driver().execute_script("window.scrollTo(0,10000)")
        time.sleep(1)
        self.bch.click_submit()



if __name__ == '__main__':
    # 打开浏览器
    driver = DriverUtil.get_driver()
    # 打开登录页面
    driver.get("http://demo.zentao.net/user-login.html")

    # 测试登录
    ulp = UserLoginProxy()
    myp = MyProxy()
    qp = QaProxy()
    bbp = BugBrowseProxy()
    bcp = BugCreateProxy()

    ulp.tester_login()
    myp.go_qa()
    qp.go_bug_browse()
    bbp.go_create_bug()
    time.sleep(3)
    bcp.create_bug("my_bug_2")

    # 退出浏览器
    time.sleep(2)
    DriverUtil.quit_driver()

