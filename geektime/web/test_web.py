from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestCeshirenSearch:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')

    def setup(self):
        self.driver.find_element(By.ID,)

    def test_search(self):
        ...

    def teardown(self):
        ...

    def teardown_class(self):
        ...