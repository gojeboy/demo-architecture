from flask import Flask
from app.config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = config_progress()

# db = SQLAlchemy(app)

# migrate = Migrate(app, db)


from app.controllers import test_controller
