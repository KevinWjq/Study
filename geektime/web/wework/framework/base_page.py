from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is not None:
            self.driver = driver
        else:
            # 远程调用chrome浏览器，绕过扫码认证进入后台，如果要使用多浏览器，可以用cookie复用
            options = Options()
            options.debugger_address = '127.0.0.1:9522'
            self.driver = webdriver.Chrome(options=options)

    def click(self, by, value):
        # todo:异常处理
        self.find_element_by(by, value).click()

    def find_element_by(self, by, value):
        # todo:异常处理
        # todo:智能判断
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, value)))
        return self.driver.find_element(by, value)
