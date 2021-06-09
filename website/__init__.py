from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() # init database
DB_NAME = "database.db"


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sfd3kjkgj kajse'  # encrypt or secure the cookies and session data related in the websit
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # SQL database is store or located in DB_NAME
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='')

    from .models import User, Note

    createDatabase(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader  # load a user using flask
    def load_user(id):
        return User.query.get(int(id))  # default look for pk

    return app


def createDatabase(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')