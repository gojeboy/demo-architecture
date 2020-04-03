from flask import Flask
from flask_script import Manager
from flask_cors import CORS
import requests
from flask_migrate import Migrate, MigrateCommand


from app.models.user import User
from app.models.address import Address


from app import app, db

migrate = Migrate(app, db)


CORS(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def reset_db():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    manager.run()

