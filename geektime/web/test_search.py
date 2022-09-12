# Generated by Selenium IDE
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get("https://ceshiren.com/")

    def setup(self):
        self.driver.find_element(By.ID, "search-button").click()

    def teardown(self):
        self.driver.find_element(By.ID, "search-button").click()
        self.driver.find_element(By.CSS_SELECTOR, '[title="清除搜索内容"]').click()

    @pytest.mark.parametrize('keyword', ['selenium', 'requests', 'appnium'])
    def test_search(self, keyword):
        self.driver.find_element(By.ID, 'search-term').send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'topic-title'))
        )
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.visibility_of_element_located(By.CSS_SELECTOR, '.fps-result-entries>div>div[2]>div>a>span>span>span')
        # )
        assert keyword in self.driver.find_element(By.CLASS_NAME, 'topic-title').text.lower()