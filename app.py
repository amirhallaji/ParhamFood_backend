
from flask import Flask
from markupsafe import escape
import os


# import other .py files
import handler.ManagerHandler as MH
import handler.UserHandler as UH
import db


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
)
app.config.from_pyfile('config.py', silent=True)
db.init_app(app)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
