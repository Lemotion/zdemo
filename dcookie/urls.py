from django.conf.urls import url

from . import views

urlpatterns = [

    # 末尾加不加  /  看公司要求
    url(r'^dcookie/$', views.login_cookie),
]