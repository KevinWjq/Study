import datetime

import pytest

from geektime.web.wework.page.member import Member
from geektime.web.wework.page.wework_page import WeWorkPage


class TestMemberAdd:
    def setup_class(self):
        self.wework = WeWorkPage()
        self.contact_page = self.wework.contact()

    def setup(self):
        self.contact_page = self.wework.portal().contact()

    @pytest.mark.parametrize('member_data', [
        {'name': 'kevin'},
        {'name': 'ceshiren.com'},
        {'name': '七七', 'account': 'sevin'}
    ])
    def test_add_member(self, member_data):
        timestamp = str(datetime.datetime.now().timestamp()).split('.')[0]
        member = Member(**member_data)
        # member.name = 'kevin'
        if member.account is None:
            member.account = member.name

        member.account = member.account + '_' + timestamp

        if member.mail is None:
            member.mail = member.account

        member.phone = timestamp + '0'

        self.contact_page.add_member(member)
        self.member_page = self.contact_page.search_member(member.name)
        member2 = self.member_page.get_member()
        assert member2.name == member.name
