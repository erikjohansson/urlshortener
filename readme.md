# URL Shortener

( a.k.a USHER :) )

A simple URL Shortener application written in Python using the Django framework.

Django is an open-source web framework that is fast, secure, and stable, with a large community behind it.

## Requirements

- Python 3.8 or higher

## How to use

- Create a python virtual environment and install dependencies

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

- Run the database migrations

  ```bash
  python manage.py migrate
  ```

- Create a superuser

  ```bash
  python manage.py createsuperuser
  ```

- Run the application

  ```bash
  python manage.py runserver
  ```
