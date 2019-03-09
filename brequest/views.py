from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):

    return HttpResponse('1.研究request请求对象 传参  1.1 10/20/拼接路径 1.2 ?a=10&b=20&a=30 1.3 json xml str 1.4 form 1.5 请求头')