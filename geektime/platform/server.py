from geektime.platform.app import app
from geektime.platform.route.auth import auth_bp
from geektime.platform.route.task import task_bp
from geektime.platform.route.testcase import testcase_bp

if __name__ == '__main__':
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(testcase_bp)
    # with app.app_context():
    #     db.create_all()
    #     user1 = User()
    #     user1.username = 'kevin788'
    #     user1.email = 'kevin77@qq.com'
    #     db.session.add(user1)
    #     db.session.commit()

    app.run(debug=True)
