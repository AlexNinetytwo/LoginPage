from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_sslify import SSLify
from datetime import timedelta


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    
    app = Flask(__name__)
    sslify = SSLify(app)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
    app.config['DRIVE_BUTTON_STATES'] = []
    
    

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Blind, Light
    
    with app.app_context():
        db.create_all()
        for module in Blind.query.all() + Light.query.all():
            app.config['DRIVE_BUTTON_STATES'].append({module.port : ''})
    
        

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

