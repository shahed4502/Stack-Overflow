First time:
* virtualenv ~/.virtualenvs/djangodev
* python3 manage.py startapp stack
* set time zone in settings by 'Asia/Dhaka'

Each time:
* source ~/.virtualenvs/djangodev/bin/activate
* Move to stack_overflow directory
* python3 manage.py runserver
* deactivate //deactivates virtual environment

migrate:
* python3 manage.py makemigrations stack
* python3 manage.py migrate

Procedure:
* create urls.py in app
* add appconfig in settings INSTALLED_APPS
* to make things modifiable by admin register the models in stack/admin.py

* to get value from html by post in view do request.POST['name of the input element']
