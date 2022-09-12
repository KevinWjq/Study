from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from geektime.app.wework.page.search_page import SearchPage


class WeWorkApp:
    def __init__(self):
        caps = {
            "platformName": "android",
            "appium:appPackage": "com.tencent.wework",
            "appium:appActivity": "com.tencent.wework.launch.LaunchSplashActivity",
            "appium:noReset": "true",
            "appium:appWaitDuration": "40000",
            "appium:newCommandTimeout": "180"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def search(self):
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/kuo").click()
        return SearchPage(self.driver)

    def close(self):
        self.driver.quit()