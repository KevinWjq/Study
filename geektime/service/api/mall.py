import requests
from requests import Response


class Mall:
    def login(self, username, password, code) -> Response:
        r = requests.post(
            url='https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            cookies={'cookie1': 'cookie1 value'},
            json={
                "username": username,
                "password": password,
                "code": code
            }
        )
        return r

    def list_users(self) -> Response:
        r = requests.get(
            'https://litemall.hogwarts.ceshiren.com/admin/user/list?page=1&limit=20&sort=add_time&order=desc',
            cookies={'X-Litemall-Admin-Token': '2ff2c852-00b9-4a15-85d5-e9ee54183ed2'},
            headers={'X-Litemall-Admin-Token': '2ff2c852-00b9-4a15-85d5-e9ee54183ed2'}
        )
        return r

    def list_orders(self):
        pass

    def logout(self):
        pass