from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app.config import Config
# from app.db import DB
# from flask_migrate import Migrate

import psycopg2

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = config_progress()


# migrate = Migrate(app, db)

from app.controllers import test_controller
