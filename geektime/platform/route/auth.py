from flask import render_template, request, Blueprint

from geektime.platform.app import app
from geektime.platform.db import db
from geektime.platform.domain.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/')
@auth_bp.route('/<name>')
def index(name):
    return render_template('hello.html', name=name, args=request.args)


@auth_bp.route('/login', methods=['POST'])
def login():
    ...


@auth_bp.route('/users/<id>')
def user_list():
    user = User.query.get(1)
    # app.logger.error(user)
    # app.logger.error(user.username)
    result = db.session.execute(db.select(User)).scalars().first()
    app.logger.error(result.username)
    # users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    # app.logger.error(users)
    return {
        'username': user.username,
        'id': user.id,
        'email': user.email
    }
