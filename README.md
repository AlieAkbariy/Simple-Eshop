# Simple-Eshop
Simple Eshop website created with [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com/)
>note! i downloaded template from [this site](https://toplearn.com/)


## Instalition
1- After you clone repository you should build [virtual-environments](https://docs.python.org/3/library/venv.html) like below:

```bash
python3 -m venv Location_of_project
```

2- this project use some python library. so, you should install django,[Pillow](https://pypi.org/project/Pillow/),[django_render_partial](https://pypi.org/project/django-render-partial/) in virtual environments.
```bash
pip install django,Pillow,django_render_partial
```

3- After that you should [collectstatic](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/) you can use code below(**you can find manage.py in project**):

```bash
python manage.py collectstatic
```

4- Then you should config database (default set sqllite3) if you want you can change it from Simple-Eshop/Eshop/Setting.
> see [this](https://docs.djangoproject.com/en/3.2/topics/db/) for more information 

5- After that you should make tables of your database
>it's so easy😉

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Usage
To run this project run this command in your terminal

```bash
python manage.py runserver
```
When you run this command it give you link click on link and enjoy it😉.
