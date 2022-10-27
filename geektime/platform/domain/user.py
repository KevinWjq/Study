from geektime.platform.db import db


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String, unique=True, nullable=False)
    email: str = db.Column(db.String)
    password = db.Column(db.String)
