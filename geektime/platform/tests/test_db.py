from geektime.app.wework.utils.log import log
from geektime.platform.app import app
from geektime.platform.db import db
from geektime.platform.domain.testcase import TestCase


def test_init():
    with app.app_context():
        db.drop_all()
        db.create_all()
        testcase = TestCase()
        testcase.name = "testcase2"
        db.session.add(testcase)
        db.session.commit()

        log.debug(db.session.execute(db.select(TestCase)).scalars().all())
