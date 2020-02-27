# 封装浏览器驱动
from selenium import webdriver
# 创建驱动工具类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtil:
    # 驱动保存
    __driver = None

    # 驱动获取
    @classmethod
    def get_driver(cls):
        # 如果__driver属性为空,这个时候没有浏览器驱动对象,无法获取
        # 先初始化浏览器驱动对象,保存在__driver
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            # cls.__driver.implicitly_wait(20)
        # 返回驱动对象
        return cls.__driver

    # 驱动销毁
    @classmethod
    def quit_driver(cls):
        # 如果__driver为空, 这个时候无法进行浏览器销毁,不用销毁
        # __driver非空的时候 才需要销毁浏览器驱动
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None


# 判断页面中是否存在"保存成功"四个
# 如果能定位到 -- 存在 -- 符合预期
# 如果不能定位到 -- 不存在 -- 不符合预期
def exists_text(text):
    driver = DriverUtil.get_driver()
    try:
        WebDriverWait(driver,5,0.5).until(lambda d:d.find_element(By.XPATH, "//*[text()='{}']".format(text)))
        # 如果能定位到 - - 存在 - - 符合预期
        return True
    except:
        # 如果不能定位到 -- 不存在 -- 不符合预期
        return False
