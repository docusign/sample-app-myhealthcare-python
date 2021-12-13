#!/bin/bash

cd backend
source venv/bin/activate

python3 manage.py runserver localhost:5001 > /dev/null 2>&1 &

cd ../frontend
npm start  > /dev/null 2>&1 &
