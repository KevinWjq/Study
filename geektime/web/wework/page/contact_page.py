from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from geektime.web.wework.framework.base_page import BasePage
from geektime.web.wework.page.member import Member
from geektime.web.wework.page.member_page import MemberPage


class ContactPage(BasePage):
    def __init__(self, driver: WebDriver):
        # 接受外部传入的driver，用于自己的自动化测试
        super().__init__(driver)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'立即邀请')))

    def add_member(self, member: Member):
        # 如果控件发生了变化或者重绘，需要显式等待合理的状态
        self.click(By.LINK_TEXT, '添加成员')
        self.find_element_by(By.NAME,'username').send_keys(member.name)
        self.find_element_by(By.NAME, 'acctid').send_keys(member.account)
        mail_element = self.find_element_by(By.NAME, 'biz_mail')
        mail_element.clear()
        mail_element.send_keys(member.mail)
        self.find_element_by(By.NAME, 'mobile').send_keys(member.phone)
        self.find_element_by(By.LINK_TEXT, '保存').click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, '立即邀请')))
        return self

    def import_contact(self, path):
        return self

    def export_contact(self):
        ...

    def delete_member(self):
        return self

    def search_member(self, keyword):
        self.driver.find_element(By.ID,'memberSearchInput').send_keys(keyword)
        return MemberPage(self.driver)
