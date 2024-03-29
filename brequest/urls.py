# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.conf.urls import url

from . import views

urlpatterns = [

    # 末尾加不加  /  看公司要求
    url(r'^brequest/$', views.login, name="login"),

    #     1.  2008/beijing/拼接路径参数 直接正则匹配
    # url(r'^brequest/(\d{4})/([a-z]+)/$', views.login_connect),


    #     2.  2008/beijing/拼接路径参数 直接正则匹配  给正则起名字 获取的时候就可以不根据顺序
    url(r'^brequest/(?P<year>\d{4})/(?P<city>[a-z]+)/$', views.login_connect),

    #     3. ?a=10&b=20&a=30 解析查询参数
    url(r'^brequest_query/$', views.login_query),

    # 4. form表单参数的 解析
    url(r'^brequest_form/$', views.login_form),

    # 5. 非form表单参数的 解析
    url(r'^brequest_not_form/$', views.login_not_form),

    #    6.请求头 信息获取
    url(r'^brequest_headers/$', views.login_header),



]
