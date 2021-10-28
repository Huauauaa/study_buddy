# study_buddy

## create project

`django-admin startproject study_buddy`

## virtualenv

### create virtual env

`virturalenv -p python3 [envname]`

### active virtual env

- win: `[envname]\Scripts\activate`
- mac: `source [envname]/bin/activate`

### freeze labs

`pip freeze > requirements.txt`

### install labs

`pip install -r requirements.txt`

## run project

`python manage.py runserver`

## templates

### include

`{% include 'navbar.html' %}`

### extends

- parent.html: `{% block content %} {% endblock %}`
- children: `{% extends 'parent.html' %} {% block content %} ... {% endblock %}`
