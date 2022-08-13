import pytest

from geektime.service.petclinic.utils.log import log
from geektime.service.wework.factory.SessionFactory import SessionFactory
from geektime.service.wework.factory.portal_factory import PortalFactory
from geektime.service.wework.model.app import App
from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.calendar_api import CalendarApi
from geektime.service.wework.model.session import Session
from geektime.service.wework.model.wework import WeWork


class TestCalendar:
    def setup_class(self):
        implement = 'service'
        wework = WeWork()
        app = App()
        # session = Session(wework, calendar_app)
        session: Session = SessionFactory.create_session(implement, wework, app)
        self.portal_api = PortalFactory.create(implement, session)

    @pytest.mark.parametrize('calendar_data', [
        {'summary': 'demo', 'color': '#0000FF','organizer': 'WangJinQi'}
    ])
    def test_add(self, calendar_data):
        calendar = Calendar(**calendar_data)
        r = self.portal_api.add_calendar(calendar)
        print(r.text)
        assert r.json()['errcode'] == 0

        cal_id = r.json()['cal_id']

        calendar_list = self.portal_api.list(cal_id)
        assert calendar in calendar_list

    def test_del(self):
        calendar_list = self.calendar_api.list()
        calendar_demo = calendar_list[0]
        calendar_demo.delete()

        calendar_list = self.calendar_api.list()
        assert calendar_demo not in calendar_list
