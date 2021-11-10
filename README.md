# study_buddy

## create project

`django-admin startproject study_buddy`

## virtualenv

### create virtual env

`virtualenv -p python3 [env_alias]`

### active virtual env

- win: `[envname]\Scripts\activate` or `source ./[envname]/Scripts/activate`
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

- parent.html: `{% block [block_alias] %} {% endblock %}`
- children: `{% extends 'parent.html' %} {% block [block_alias] %} ... {% endblock %}`

## 返回上一步

- `<a href="{{request.META.HTTP_REFERER }}" >Back</a>`
- `return redirect(request.META.HTTP_REFERER)`

## 列表的长度

`{{ some_list|length }}`

## 跳转页面带参数

`redirect('{}?flag=True'.format(reverse('new_view'))`
