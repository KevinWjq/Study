from dataclasses import asdict

from flask import Blueprint, request
from flask_sqlalchemy.query import Query

from geektime.platform.app import app
from geektime.platform.db import db
from geektime.platform.domain.testcase import TestCase

testcase_bp = Blueprint("testcase", __name__)


@testcase_bp.route('/testcase/<id>', methods=['GET'])
def case_get(id):
    query: Query = TestCase.query
    testcase = query.filter(TestCase.id == id).scalar()
    app.logger.error(testcase)
    return {
        'errcode': 0,
        'data': asdict(testcase)
    }


@testcase_bp.route('/testcase', methods=['POST'])
def case_post():
    testcase = TestCase()
    testcase.name = request.json['name']
    db.session.add(testcase)
    db.session.commit()
    return {
        'errcode': 0
    }
