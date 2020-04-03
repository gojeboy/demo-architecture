from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_progress
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config_progress()
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.controllers import test_controller
