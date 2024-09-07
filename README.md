# Learning Django API (Django, REST and MySQL)

Creating a simple CRUD API with Django, REST and MySQL.



```
sudo apt update
sudo apt install snapd

python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install Django
pip3 install djangorestframework
pip3 install django-cors-headers
sudo apt-get install mysql-client
sudo snap install mysql-workbench-community

django-admin startproject worldCountries .
python3 manage.py startapp countries

mysql-workbench
```


```
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'secret';
CREATE USER 'django_admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'test123';
sudo mysql -u root -p

mysql-workbench
Create schema countriesdb
Create and give django_admin DBA roles inmysql-workbench
python3 manage.py migrate

python3 manage.py makemigrations countries
python3 manage.py migrate countries
```

```
settings.py

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://192.168.244.132',  # If your app is served on a specific port
)

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "countries.apps.CountriesConfig",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "countriesdb",
        "USER": "django_admin",
        "PASSWORD": "test123",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

```
countries/models.py
from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    capital = models.CharField(max_length=50, blank=False, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
```


```
serializers.py
from rest_framework import serializers
from countries.models import Countries

class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = ('id', 'name', 'capital' )
```

```
countries/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/countries', views.countries_list),
    path('api/countries/<int:pk>', views.countries_detail)
]
```

```
project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('countries.urls')),
]
```

```
countries/admin.py
from django.contrib import admin
from countries.models import Countries

# Register your models here.
admin.site.register(Countries)
```


```
Postman

http://127.0.0.1:8000/api/countries

raw POST:

{
    "name" : "Denmark",
    "capital" : "Copenhagen"
}
```
