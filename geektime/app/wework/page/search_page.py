from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword) -> list[dict]:
        self.driver.find_element(AppiumBy.ID, 'j65').send_keys(keyword)
        result_list = []
        for item in self.driver.find_elements(AppiumBy.ID, 'ezy'):
            r = {}
            cul_list = item.find_elements(AppiumBy.ID, 'cul')
            if len(cul_list) == 0:
                r['type'] = 'app'
            else:
                r['desc'] = cul_list[0].text
                if '包含' in r['desc']:
                    r['type'] = 'group'
                elif '相关聊天记录' in r['desc']:
                    r['type'] = 'chat'
                else:
                    r['type'] = 'contact'
            r['name'] = item.find_element(AppiumBy.XPATH,
                                          "//*[contains(@resource-id,'g9n')]/*[contains(@class,'Text')]").text
            result_list.append(r)
        # r['name'] = self.driver.find_element(AppiumBy.ID, 'g9n').\
        #     find_element(AppiumBy.CLASS_NAME,'android.widget.TextView').text
        # for item in self.driver.find_elements(AppiumBy.XPATH,"//*[contains(@resource-id,'g9n')]/*[contains(@class,'Text')]"):
        #     r={'name':item.text}
        #     result_list.append(r)
        return [item for item in result_list if item['type'] == 'contact']

    def search_app(self, keyword) -> list[dict]:
        ...

    def clear_search(self):
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[contains(@resource-id,"kv6")]//*[contains(@resource-id,"j64")]').click()
