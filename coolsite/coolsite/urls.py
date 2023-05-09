from django.contrib import admin
from django.urls import path, include
from cars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
]