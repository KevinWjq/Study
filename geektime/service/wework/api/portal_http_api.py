from dataclasses import asdict

import requests

from geektime.service.petclinic.utils.log import log
from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.portal import Portal


class PortalHttpApi(Portal):
    def add_calendar(self, calendar: Calendar):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/add',
            params={'access_token': self.session.get_token()},
            json={'calendar': asdict(calendar)}
        )
        log.debug(f'add_calendar = {r.text}')
        return r

    def list(self, calendar_id_list):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/get',
            params={'access_token': self.session.get_token()},
            json={'cal_id_list': calendar_id_list}
        )
        calendar_list = []
        for item in r.json()['calendar_list']:
            canlendar = Calendar()
            canlendar.color = item['color']
            canlendar.summary = item['summary']
            canlendar.organizer = item['organizer']
            calendar_list.append(canlendar)
        log.debug(f'calendar_list = {calendar_list}')
        return calendar_list

    def get(self, calendar_id):
        return self.list(calendar_id)[0]

