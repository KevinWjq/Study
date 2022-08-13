from geektime.service.wework.model.calendar import Calendar
from geektime.service.wework.model.session import Session


class Portal:
    def __init__(self,session:Session):
        self.session=session

    def add_calendar(self, calendar: Calendar):
        ...

    def list(self,calendar_id_list):
        ...

    def get(self,calendar_id):
        ...