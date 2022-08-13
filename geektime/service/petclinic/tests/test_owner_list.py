from copy import copy
from geektime.service.petclinic.api.owners import Owners
from geektime.service.petclinic.tests.test_data import owner_common
from geektime.service.petclinic.tests.test_owner import TestOwner


class TestOwnersList(TestOwner):
    def setup_class(self):
        super(TestOwnersList, self).setup_class(self)
        # "所有测试用例前只执行一次"
        # 引入业务模型
        self.owners = Owners()

        # 清理数据
        self.owners.clear('Seven')

        # 初始化数据
        owner1 = copy(owner_common)
        self.owners.add(owner1)

        owner2 = copy(owner1)
        owner2.firstName = 'Qiiii'
        self.owners.add(owner2)


    def setup(self):
        """setup"""

    def teardown(self):
        """teardown"""

    def teardown_class(self):
        """clear"""
        self.owners.clear('Seven')

    def test_search_query_null(self):
        r = self.owners.list('')
        assert len(r) > 0

    def test_search_result_null(self):
        r = self.owners.list('ceshiren.com')
        assert r == []

    def test_search_result_single(self):
        r = self.owners.list('Ke')
        print(r)
        assert len(r) == 1
        assert r[0].lastName == 'Ke'

    def test_search_result_multi(self):
        r = self.owners.list('Seven')
        assert len(r) == 2
