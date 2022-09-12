import pytest

from geektime.app.wework.page.wework_app import WeWorkApp
from geektime.app.wework.utils.log import log


class TestSearch():
    def setup_class(self):
        self.search_app = WeWorkApp()
        self.search_page = self.search_app.search()

    def teardown(self):
        self.search_page.clear_search()

    def teardown_class(self):
        self.search_app.close()

    @pytest.mark.parametrize('keyword,expect', {
        ('qiqi','七七'),
        ('wjq','王瑾琪'),
        ('ceshiren','ceshiren')
    })
    def test_search_contact(self, keyword,expect):
        r = self.search_page.search(keyword)
        contact_list = [item for item in r if item['type']=='contact']
        log.debug(r)
        assert expect in contact_list

    @pytest.mark.parametrize('keyword,expect', {
        ('mamahaha','')
    })
    def test_search_contact_null(self, keyword,expect):
        r = self.search_page.search(keyword)
        contact_list = [item for item in r if item['type'] == 'contact']
        log.debug(r)
        assert len(contact_list)==0
