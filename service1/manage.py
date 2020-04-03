from flask import Flask
from flask_script import Manager
from flask_cors import CORS
import requests

# from flask_migrate import Migrate, MigrateCommand


from app.models.user import User
from app.config import *

from app import app, db

# migrate = Migrate(app, db)


CORS(app)
manager = Manager(app)
# manager.add_command("db", MigrateCommand)


@manager.command
def test():
    print("Testing is good")


@manager.command
def run():
    app.run(host="0.0.0.0", debug=True, port=5000)


if __name__ == "__main__":
    manager.run()
