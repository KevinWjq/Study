from geektime.platform.db import db


# 执行结果
class Execution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
