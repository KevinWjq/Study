from flask import Flask, render_template, request

from geektime.service.platform.db import db, User

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.secret_key = 'kevin'
# initialize the app with the extension
db.init_app(app)


@app.route('/')
def index(name):
    return render_template('hello.html', name=name, args=request.args)


@app.route('/testcase', methods=['GET'])
def testcase_get():
    ...


@app.route('/testcase', methods=['POST'])
def testcase_get():
    ...


@app.route('/login', methods=['POST'])
def login():
    ...


@app.route('/task', methods=['POST'])
def task_post():
    ...


@app.route('/users/<id>')
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


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    #     user1 = User()
    #     user1.username = 'kevin788'
    #     user1.email = 'kevin77@qq.com'
    #     db.session.add(user1)
    #     db.session.commit()

    app.run(debug=True)
