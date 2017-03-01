# eduya
Create a hub for academic resources for Purdue students, from tutor listings in the area to SI sessions, Office Hours, and other campus resources

To run the server: `python manage.py runserver`

Creating a python virtual environment: `virtualenv venv`
Activating the python virtualenv: `source venv/bin/activate`
Installing the necessary libraries: `venv/bin/pip install -r requirements.txt`
If new dependencies are added, make note of them by updating requirements.txt: `pip freeze > requirements.txt`

Installing the requirements: `sudo pip3 install -r requirements.txt`

Setting up the database:
Within the postgresql shell:
```
create user eduyadbadmin with password '123456';
create database eduya;
grant all on database eduya to eduyadbadmin;
\q
```

