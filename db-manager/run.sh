#!/bin/bash

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

echo "Done setting up db"

python manage.py reset_db

echo "Done resetting db"