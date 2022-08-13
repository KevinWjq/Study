from geektime.service.wework.model.schedule import Schedule


class ScheduleApi:
    @classmethod
    def add(cls, schedule: Schedule):
        ...

    def update(self, schedule: Schedule):
        ...

    def delete(self):
        ...

    @classmethod
    def list(cls):
        ...