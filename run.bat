@echo off
cd venv\scripts
call activate
cd ..
cd ..
cd run
python manage.py runserver 8080