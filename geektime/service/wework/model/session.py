from geektime.service.petclinic.utils.log import log
from geektime.service.wework.model.app import App
from geektime.service.wework.model.wework import WeWork


class Session:
    _access_token = None

    def __init__(self,wework: WeWork,app:App):
        self._access_token=self.refresh_token(wework, app)
        Session._access_token=self._access_token
        log.debug(f"token = {self._access_token}")

    def refresh_token(self,wework: WeWork,app:App):
        ...

    def get_token(self):
        return self._access_token

    @classmethod
    def get_global_token(cls):
        return cls._access_token

