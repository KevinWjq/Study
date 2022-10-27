from dataclasses import dataclass

from geektime.platform.db import db


# 测试用例
@dataclass
class TestCase(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, unique=True, nullable=False)
    task = db.relationship("Task", back_populates="testcase")
