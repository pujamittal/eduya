# eduya
Create a hub for academic resources for Purdue students, from tutor listings in the area to SI sessions, Office Hours, and other campus resources

To run the server: `python manage.py runserver`

Creating a python virtual environment: `virtualenv venv`
Activating the python virtualenv: `source venv/bin/activate`
Installing the necessary libraries: `venv/bin/pip install -r requirements.txt`
If new dependencies are added, make note of them by updating requirements.txt: `pip freeze > requirements.txt`

Installing the requirements: `sudo pip3 install -r requirements.txt`

Copy the config example file: `cp eduya/eduya/settings.example.py eduya/eduya/settings.py` and change necessary settings if needed

In another terminal(cloud9 directions):
```
sudo service postgresql start
psql
```

Setting up the database:
Within the postgresql shell:
```
create user eduyadbadmin with password '123456';
create database eduya;
grant all on database eduya to eduyadbadmin;
\q
```

To insert test data into database (for demo purposes):
```
python manage.py shell
import create_test_data
```

URL endpoints:
```
/
/admin/
/reset-password/
/reset-password/done/
/reset-password/confirm/
/reset-password-complete/
/register/
/login/
/logout/
/reset/
/posts/
/posts/new/
/posts/<post_id>/
/tutors/
/tutors/<tutor_id>/
/profile/
/my-courses/
/my-listings/
/courses/
/professors/
```