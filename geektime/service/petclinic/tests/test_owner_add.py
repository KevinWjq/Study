from copy import copy

import pytest
from geektime.service.petclinic.api.owner import Owner
from geektime.service.petclinic.api.owners import Owners
from geektime.service.petclinic.tests.test_data import owner_common
from geektime.service.petclinic.tests.test_owner import TestOwner


class TestOwnersAdd(TestOwner):
    def setup_class(self):
        super(TestOwnersAdd, self).setup_class(self)
        # "所有测试用例前只执行一次"
        # 引入业务模型
        self.owners = Owners()
        self.owners.clear('Seven')

    def setup(self):
        """setup"""

    def teardown(self):
        """teardown"""

    def teardown_class(self):
        """clear"""
        self.owners.clear('Seven')

    @pytest.mark.parametrize('owner', [
        {'telephone': '607000000', 'firstName': 'hali'},
        {'telephone': '607000000', 'firstName': 'qiuqiu'},
        {'telephone': '607000000', 'firstName': 'sisisi'},
        {'telephone': '607000000', 'firstName': 'JOJOJO'}
    ])
    def test_add_success(self, owner):
        owner1 = copy(owner_common)
        owner_param = Owner(**owner)
        owner1.telephone = owner_param.telephone
        owner1.firstName = owner_param.firstName

        r = self.owners.add(owner1)
        assert r.status_code == 201

    @pytest.mark.parametrize('owner', [
        {'telephone': '607000000', 'firstName': ''},
        {'telephone': 'abc', 'firstName': 'a'},
        {'telephone': '607000000', 'firstName': 'a f'},
        {'telephone': '607000000', 'firstName': '11'}
    ])
    def test_add_failed(self, owner):
        owner1 = copy(owner_common)
        owner_param = Owner(**owner)
        owner1.telephone = owner_param.telephone
        owner1.firstName = owner_param.firstName
        r = self.owners.add(owner1)
        assert r.status_code != 201
