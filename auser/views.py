from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls.base import reverse


def index(request):

    # 路由的反解析 : 倒着 找路径 是多少?
    # 1.判断 /index/
    # 2.重定向

    print(reverse("login"))

    return  HttpResponse('第一个 django的应用!')