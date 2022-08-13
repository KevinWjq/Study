from geektime.service.api.mall import Mall


class TestMall:
    def setup_class(self):
        print('suite级别数据初始化')
        self.mall = Mall()

    def setup(self):
        print('case级别初始化')

    def test_login(self):
        r = self.mall.login("admin123", 'admin123', '')
        assert r.status_code == 200
        assert r.json()['errmsg'] == '成功'
        assert r.json()['data']['adminInfo']['nickName'] == 'admin123'

    def test_login_fail(self):
        r = self.mall.login('admin123', 'wrong', '')
        assert r.status_code == 200
        assert r.json()['errmsg'] == '用户帐号或密码不正确'

    def test_list_users(self):
        r = self.mall.list_users()
        assert r.status_code == 200

    def teardown(self):
        print('case级别数据清理')

    def teardown_class(self):
        print('suite级别数据清理')
