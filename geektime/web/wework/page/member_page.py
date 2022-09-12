from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from geektime.web.wework.framework.base_page import BasePage
from geektime.web.wework.page.member import Member


class MemberPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'member_display_cover_detail_name')))

    def get_name(self):
        ...

    def get_account(self):
        ...

    def save_member(self, member):
        ...

    def get_member(self):
        member = Member()
        member.name = self.driver.find_element(By.CLASS_NAME, 'member_display_cover_detail_name').text
        member.account = self.driver.find_elements(By.CLASS_NAME,
                                                   'member_display_cover_detail_bottom')[1].text.replace('帐号：', '')
        member.mail = self.driver.find_element(By.XPATH, '//div[text()="企业邮箱："]/following-sibling::div').text
        member.phone = self.driver.find_element(By.CSS_SELECTOR,
                                                '.member_display_item_Phone>.member_display_item_right').text
        return member
