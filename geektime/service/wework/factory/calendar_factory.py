from geektime.service.wework.api.calendar_http_api import CalendarHttpApi
from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.calendar_api import CalendarApi
from geektime.service.wework.model.session import Session


class CalendarFactory:
    @classmethod
    def create(cls, implement, session: Session, calendar: Calendar):
        if implement == 'service':
            return CalendarHttpApi(session, calendar)
        else:
            return CalendarApi(session, calendar)
