import requests

from geektime.app.wework.utils.log import log
from geektime.platform.app import app
from geektime.platform.db import db

target = 'http://127.0.0.1:5000/'


class TestCase:
    def setup_class(self):
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_post(self):
        r = requests.post(
            target + '/testcase',
            json={
                'name': 'testcase7'
            }
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0

    def test_get(self):
        r = requests.get(
            target + '/testcase/4'
        )
        log.debug(r.text)
        assert r.json()['errcode'] == 0
        assert r.json()['data']['name'] == 'testcase5'
