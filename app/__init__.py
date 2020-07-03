from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from .request import configure_request

# intializing the app
# app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)

bootstrap = Bootstrap()


# from app import views
# from app import error
def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms
    # Registering the blueprint
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    configure_request(app)

    return app