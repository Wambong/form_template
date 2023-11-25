# form_template
1).download the zipfile from github and unzip it.

2). open the project in an ide recommend pycharm and navigate to ..templates\form_validate> 
3). run pip install -r requirements.txt to install all the requirements
4) run python manage.py runserver.
5). open a browser and navigate to http://127.0.0.1:8000/form_templates/ where forms and field can be submitted
6) you can create a super user with the following commands >python manage.py createsuperuser< then fill out the username, email and password.
7) use the superuser you just created in step 6 to login into the admin site http://127.0.0.1:8000/admin/form_templates/formtemplate/ to see the forms stored in the database.
8) i used sqlite3 daatbase not tinydb because it comes directly with django and doesn't require setting up.


.

