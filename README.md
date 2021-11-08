# study_buddy

## create project

`django-admin startproject study_buddy`

## virtualenv

### create virtual env

`virturalenv -p python3 [env_alias]`

### active virtual env

- win: `[env_alias]\Scripts\activate`
- mac: `source [env_alias]/bin/activate`

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

- parent.html: `{% block [block_alias] %} {% endblock %}`
- children: `{% extends 'parent.html' %} {% block [block_alias] %} ... {% endblock %}`

## 返回上一步

- `<a href="{{request.META.HTTP_REFERER }}" >Back</a>`
- `return redirect(request.META.HTTP_REFERER)`

## 列表的长度

`{{ some_list|length }}`
