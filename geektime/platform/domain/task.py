from dataclasses import dataclass

from geektime.platform.db import db


# 任务调度
@dataclass
class Task(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, unique=True, nullable=False)
    testcase_id = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    testcase = db.relationship("TestCase", back_populates="tasks")
