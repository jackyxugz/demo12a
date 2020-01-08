#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01.urls', namespace='app01')),
]
