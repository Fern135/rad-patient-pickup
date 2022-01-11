from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

from config import *  # config classes


db = SQLAlchemy()
DB_NAME = "database.db" # temp db

# mysql connection
mysql_db_conn = f'mysql+pymysql://{Config.username}:{Config.password}@{Config.ip}/{Config.db}'

dev_db = f'sqlite:///{DB_NAME}'

dev_Key = DevelopmentConfig.SECRET_KEY

production_key = ProductionConfig.SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = dev_Key
    app.config['SQLALCHEMY_DATABASE_URI'] = dev_db

    # configuring email sending
    # app.config['MAIL_SERVER']     = Config.MAIL_SERVER
    # app.config['MAIL_PORT']       = Config.MAIL_PORT
    # app.config['MAIL_USERNAME']   = Config.MAIL_USERNAME
    # app.config['MAIL_PASSWORD']   = Config.MAIL_PASSWORD
    # app.config['MAIL_USE_TLS']    = Config.MAIL_USE_TLS
    # app.config['MAIL_USE_SSL']    = Config.MAIL_USE_SSL

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Patient

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')