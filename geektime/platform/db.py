from flask_sqlalchemy import SQLAlchemy

from geektime.platform.app import app

# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)
