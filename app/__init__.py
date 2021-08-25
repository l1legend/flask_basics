# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_type): #dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    #C:\Users\C-TSJN897\Desktop\Learn to build scalable Python Web Applications with Flask, PostgreSQL, SQLAlchemy, git, and Heroku with Awesome Project\config
    app.config.from_pyfile(configuration)

    db.init_app(app) #bind database to flask app

    from app.catalog import main # import blueprint
    app.register_blueprint(main) # register blueprint

    return app