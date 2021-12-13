#!/bin/bash -e

echo "...installing"

cd backend
python3 -m venv venv
source venv/bin/activate

pip3 install --upgrade pip
pip3 install django
pip3 install djangorestframework
pip3 install django-cors-headers

pip3 install wheel  # Without wheel pylint installation failed
pip3 install pylint

pip3 install docusign-esign

pip3 install python-dotenv

pip3 install gunicorn

cd ../frontend
npm install

echo "ok"