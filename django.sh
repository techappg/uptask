#!/bin/bash

cd /home/uptask

git pull

source env/bin/activate

pip install -r requirements.txt

python manage.py makemigrations merge --noinput

python manage.py migrate

python manage.py test
