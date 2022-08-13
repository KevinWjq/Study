from geektime.service.wework.api.portal_http_api import PortalHttpApi
from geektime.service.wework.model.portal import Portal
from geektime.service.wework.model.session import Session


class PortalFactory:
    @classmethod
    def create(cls, implement, session: Session):
        if implement == 'service':
            return PortalHttpApi(session)
        else:
            return Portal(session)
