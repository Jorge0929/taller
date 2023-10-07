from flask import Flask
from . import config

 
def create_app(Config_class=config):
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    from .blueprints import routes
    app.register_blueprint(routes.bp)
    return app
