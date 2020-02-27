from selenium.webdriver.support.wait import WebDriverWait

from tool.utils import DriverUtil


# 页面基类 元素对象的操作
# 对象库层(元素定位)   操作层(元素操作)   业务层(页面业务)

# 基类中封装的是公共的
# 对象库层(元素定位)
class BasePage:
    # 获取到浏览器驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    # 元素定位
    def base_find_element(self, loc, time=20):
        # loc = (定位策略,定位依据)
        # self.driver.find_element(定位策略,定位依据)
        # 元素定位要有 元素等待的效果
        # 隐式等待全局的 ,等待时长定死的,不灵活
        # 精确设置具体定位的等待效果需要使用显式等待
        # 显式等待  -> 关闭隐式等待
        wdw = WebDriverWait(self.driver, timeout=time, poll_frequency=0.5)
        element = wdw.until(lambda d: d.find_element(loc[0], loc[1]))
        return element


# 操作层(元素操作)
class BaseHandle:
    # 元素操作
    # 输入
    def base_input_text(self, element, text):
        # 给某个元素输入某些内容
        # 不会自动提示 ,手写正确
        element.clear()
        element.send_keys(text)

    # 点击
    def base_click_element(self, element):
        # 点击某个元素
        # # 不会自动提示 ,手写正确
        element.click()

