# drf pagination project #

![alt_text](https://img.shields.io/badge/Django_Rest_Framework-blue)
![alt_text](https://img.shields.io/badge/Pagination-yellow)
![alt_text](https://img.shields.io/badge/Python-red)
![alt_text](https://img.shields.io/badge/Teravision-blue)

## Introduction ##

The aim of this project is to show the power and ability of Django-Rest framework's pagination to paginate diverse registers in an API.

This project will be the `pagination` boilerplate to use in different projects.

REST framework includes support for customizable pagination styles. This allows you to modify how large result sets are split into individual pages of data.

The pagination API can support either:

- Pagination links that are provided as part of the content of the response.
- Pagination links that are included in response headers, such as Content-Range or Link.

The built-in styles currently all use links included as part of the content of the response. This style is more accessible when using the browsable API.

`Note` Every register that we will create with this api will be stored in a sqlite database, which is build by default, if you want to use another database just check `drf_pagination_project/settings.py` and change at your preferences.

## Setting up the project ##

### 1. We'll assume you already have Django and DRF installed. If not, you can install them using pip ###

``` bash
pip install django djangorestframework
```

### 2. Create a Django project ###

```bash
django-admin startproject drf_pagination_project
cd drf_pagination_project
```

### 3. Create a Django app ###

```bash
python manage.py startapp api
```

### 4. Configure Django Settings ###

Open `drf_pagination_project/settings.py` and add 'rest_framework' to the `INSTALLED_APPS` list.

```bash
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'api',
]
```

### 5. Create a model ###

For this example, let's create a simple model for a list of items. In `api/models.py`:

```bash
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
```

### 6. Create Serializers ###

Create a serializer to convert the model data into JSON format. In `api/serializers.py`:

```bash
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
```

### 7. Create Views ###

Create a view to handle item listing. In `api/views.py`:

```bash
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
```

### 8. Create URLs ###

Create a URL configuration for your API in `api/urls.py`:

```bash
from django.urls import path
from .views import ItemList

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
]
```

### 9. Configure Project URLs ###

Include your app's URLs in the project's URL configuration. In `drf_pagination_project/urls.py`:

```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

### 10. Run Migrations ###

Run migrations to create the database tables for your model:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 11. Configure Pagination ###

Open `api/views.py` and add the following line to the ItemList class to configure pagination:

```bash
from rest_framework.pagination import PageNumberPagination

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = PageNumberPagination  # Add this line for pagination
    pagination_class.page_size = 1 #How many items will be showed in the page
```

### 12. Run the Development Server ###

Start the development server:

```bash
python manage.py runserver
```

Your API is now available at <http://localhost:8000/api/items/>. You can access the paginated results by appending ?page=<page_number> to the URL.

That's it! You've created a Django Rest Framework project with pagination. You can further customize the pagination settings or add authentication as per your project requirements
