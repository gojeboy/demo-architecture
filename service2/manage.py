from flask_script import Manager
from flask_cors import CORS
from app import app, db
import requests

# from flask_migrate import Migrate, MigrateCommand

from app.models.address import Address


CORS(app)
# migrate = Migrate(app, db)

CORS(app)
manager = Manager(app)
# manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run(host="0.0.0.0", port=5001)


if __name__ == "__main__":
    manager.run()
