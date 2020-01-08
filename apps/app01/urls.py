#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
from django.urls import path
# 配置媒体文件路径
from django.views.static import serve
from demo12a.settings import MEDIA_ROOT
from .views import GetTuWenView

app_name = 'app01'

urlpatterns = [
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    path('getdata/', GetTuWenView.as_view(), name='app01'),
]