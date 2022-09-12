from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRecordTestCase:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = 'com.google.android.deskclock'
        caps["appActivity"] = 'com.android.deskclock.DeskClock'
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def setup(self):
        ...

    def test_add_clock(self):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="时钟").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="闹钟").click()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "添加闹钟")))
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="添加闹钟").click()
        self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((AppiumBy.ID, "com.google.android.deskclock:id/edit_label")))
        self.driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/edit_label").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/label_input_field").send_keys('kevin')
        self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()

    def teatdown(self):
        ...
