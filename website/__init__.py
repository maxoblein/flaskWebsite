from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    #create an instance of a flask app
    app = Flask(__name__)
    #setup config
    app.config['SECRET_KEY'] = '65328745'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app=app)

    return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')
