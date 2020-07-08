from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# # intializing the app
# 
bootstrap = Bootstrap()
db = SQLAlchemy()

# from app import views
# from app import error

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    db.init_app(app)

    # load main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # load authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    from .request import configure_request
    configure_request(app)

    return app



