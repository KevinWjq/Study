import pytest

from geektime.service.wework.factory.SessionFactory import SessionFactory
from geektime.service.wework.factory.calendar_factory import CalendarFactory
from geektime.service.wework.factory.portal_factory import PortalFactory
from geektime.service.wework.model.app import App
from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.schedule import Schedule
from geektime.service.wework.model.session import Session
from geektime.service.wework.model.wework import WeWork


class TestSchedule:
    def setup_class(self):
        implement = 'service'
        wework = WeWork()
        app = App()

        # session = Session(wework, calendar_app)
        session: Session = SessionFactory.create_session(implement, wework, app)
        self.portal_api = PortalFactory.create(implement, session)

        calendar_data_default = {'summary': 'demo_default', 'color': '#000000', 'organizer': 'WangJinQi'}
        calendar = Calendar(**calendar_data_default)
        r = self.portal_api.add_calendar(calendar)
        calendar_id = r.json()['cal_id']
        # self.calendar_default = self.portal_api.get(calendar_id)
        self.calendar_api = CalendarFactory.create(implement, session, calendar)

    @pytest.mark.parametrize('calendar_data', [
        {'summary': 'demo', 'color': '#0000FF', 'organizer': 'WangJinQi'}
    ])
    def test_add(self, schedule_data):
        schedule = Schedule(**schedule_data)
        r = self.calendar_api.add_schedule(schedule)
        assert r


    # def test_del(self):
    #     calendar_list = self.calendar_api.list()
    #     calendar_demo = calendar_list[0]
    #     calendar_demo.delete()
    #
    #     calendar_list = self.calendar_api.list()
    #     assert calendar_demo not in calendar_list
