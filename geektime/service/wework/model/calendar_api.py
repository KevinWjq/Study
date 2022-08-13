from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.schedule import Schedule
from geektime.service.wework.model.schedule_api import ScheduleApi
from geektime.service.wework.model.session import Session


class CalendarApi:

    def __init__(self, session: Session, calendar: Calendar):
        self.session = session
        self.calendar = calendar

    def set_session(self, session: Session):
        self.session = session

    @classmethod
    def add(cls, calendar: Calendar):
        ...

    def update(self, calendar: Calendar):
        ...

    def delete(self):
        ...

    @classmethod
    def list(cls):
        ...

    def add_schedule(self, schedule: Schedule):
        ...
