# Admin User
A Basic web application to create a user.


## Features

* An Admin login page
* Validate ID and Password
* If Valid, redirect to the profile page.
* If Invalid, redirect to a Signup page.
* Post Login/Signup, display all existing User ID on profile page using a dropdown list.
* Delete button to delete the selected User ID from the database.
* Logout.


create and start a a virtual environment

```bash
virtualenv env --no-site-packages

source env/bin/activate
```

Install the python package requirements using `pip`.

```bash
pip install -r requirements.txt
```

Run the migrate command to create database tables.

```bash
python manage.py migrate
```

Use the `createsuperuser` command to create a user who has superuser privileges.

```bash
python manage.py createsuperuser
```

Finally run the server using the `runserver` command.

```bash
python manage.py runserver 0.0.0.0:8000
```
