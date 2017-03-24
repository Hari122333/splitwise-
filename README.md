# splitwise-

Steps to set up  

sudo apt-get update  
sudo apt-get install python-django  

django-admin startproject projectname  
cd projectname  

*** Strongly Recommend Pycharm platform ****

create database splitwise, change the username and password in the splitwise/setting

python makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000  

http://0.0.0.0:8000/admin/


