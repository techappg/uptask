#!/bin/bash

if [ -d "env" ]
then
    echo "Python virtual environment exists."
else
    echo "Creating Python virtual environment."
    virtualenv -p python3.8 env
fi

source env/bin/activate

pip install -r requirements.txt

python manage.py makemigrations merge --noinput

python manage.py migrate

python manage.py test
