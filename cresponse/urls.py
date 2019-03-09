# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url

from . import views

urlpatterns = [

    # 末尾加不加  /  看公司要求
    url(r'^cresponse/$', views.custom_response),

    #     2. json_response
    url(r'^cresponse_json/$', views.response_json),

    #     3. 重定向 resposne
    url(r'^cresponse_redirect/$', views.response_redirect),


]
