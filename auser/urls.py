# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url

from . import views

urlpatterns = [

    # 末尾加不加  /  看公司要求
    url(r'^auser/$', views.index, name="redirecturl")
]
