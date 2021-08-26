import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bootstrap import Bootstrap
#from flask_migrate import Migrate

db = SQLAlchemy()
bootstrap = Bootstrap()
# migrate = Migrate()



def create_app(config_type): #dev, test, or prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app) # bind database to flask app
    #bootstrap.init_app(app) # initialize boostrap
    # migrate.init_app(app, db)

    from app.catalog import main
    app.register_blueprint(main)

    return app



