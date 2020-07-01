from flask import Flask
from config import DevelopmentConfig
from flask_bootstrap import Bootstrap

# intializing the app
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

bootstrap = Bootstrap(app)


from app import views
from app import error