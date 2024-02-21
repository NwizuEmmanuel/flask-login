from flask import Flask, render_template
from .views.index import index

def create_app():
    app = Flask(__name__)
    # app.config["SECRET_KEY"] = "dev"
    # app.config["Debug"] = True

    app.register_blueprint(index, url_prefix="/")

    return app