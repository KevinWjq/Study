from dataclasses import asdict

import requests

from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.calendar_api import CalendarApi
from geektime.service.wework.model.schedule import Schedule


class CalendarHttpApi(CalendarApi):
    # @classmethod
    # def add(cls, calendar: Calendar):
    #     r = requests.post(
    #         'https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/add',
    #         params={'access_token': Session.get_global_token()}
    #     )

    def add_schedule(self, schedule: Schedule):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/oa/schedule/add',
            params={'access_token': self.session.get_token()},
            json={'schedule': asdict(schedule)}
        )
        return r

    def add(cls, calendar: Calendar):
        ...
