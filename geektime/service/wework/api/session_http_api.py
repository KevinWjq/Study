import requests

from geektime.service.wework.model.app import App
from geektime.service.wework.model.session import Session
from geektime.service.wework.model.wework import WeWork


class SessionHttpApi(Session):
    def refresh_token(self, wework: WeWork, app: App):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': wework.corpid,
                'corpsecret': app.secret
            }
        )
        return r.json()['access_token']
