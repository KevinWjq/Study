import base64
import json
from dataclasses import dataclass, field
import requests
from requests import Response as RequestResponse
from geektime.service.petclinic.utils.data import Data
from geektime.service.petclinic.utils.log import log


# 二次封装request


@dataclass
class Request:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    data: dict = None
    headers: dict = field(default_factory=dict)
    type: str = 'json'

    def send(self):
        # 实现requests库的便捷封装
        env = Data.load_yaml('data/env.yaml')
        self.host = env[env['default']]

        raw = None
        if self.type == 'json':
            self.headers['Content-Type'] = 'application/json'
            if self.data is None:
                raw = None
            else:
                raw = json.dumps(self.data)
                # 加密
                # raw = base64.encodestring(raw)
        elif self.type == 'xml':
            # 数据格式处理
            ...
        else:
            raise Exception('Not exist format' + self.type)

        log.debug(self)
        requests_response = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.query,
            headers=self.headers,
            data=raw
        )

        r = Response(requests_response)
        log.debug(r.text)
        return r


@dataclass
class Response:
    def __init__(self, requests_response):
        self.r: RequestResponse = requests_response

    def json(self):
        return self.r.json()

    # 解密
    def data(self):
        return json.loads(base64.decode(self.r.text))

    @property
    def status_code(self):
        return self.r.status_code

    @property
    def text(self):
        return self.r.text
