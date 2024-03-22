@echo off
cd venv\scripts
call activate
cd ..
cd ..
python manage.py runserver 8080