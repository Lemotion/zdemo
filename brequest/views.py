from django.http.response import HttpResponse
from django.shortcuts import render
import json


# 5.请求头 信息获取
def login_header(request):
    # request.META
    # print(request.META)
    print(type(request.META))

    # 交互的个数
    print(request.META['CONTENT_TYPE'])

    # 获取 request的其他属性
    print('获取当前请求方式----:', request.method)
    print('获取当前路径----:', request.path)

    return HttpResponse('5.请求头 信息获取')


# 4.  json xml str
def login_not_form(request):
    # 解析 非form表单的参数  request.body 返回的对象是  二进制 bytes\
    b_data = request.body
    print(b_data)
    print(type(b_data))
    print(b_data.decode())

    # 如果 参数 是 json的 ; bytes--str--dict
    str_one = b_data.decode()
    dict_data = json.loads(str_one)

    print(dict_data)
    print(type(dict_data))

    return HttpResponse('4.  json xml str ')


# 3. 请求体 ---form表单参数的 解析
def login_form(request):
    params = request.POST
    print(params)
    print(type(params))
    print(params.get('b'))
    print(params.getlist('a'))

    return HttpResponse('3. form表单参数的 解析')


# 2. ?a=10&b=20&a=30 解析查询参数
def login_query(request):
    # 解析查询参数 request.GET 属性 -->返回类型  django.http.request.QueryDict 支持一键多值
    params = request.GET
    print(params)
    print(type(params))
    print(params.get('b'))
    print(params.getlist('a'))

    return HttpResponse('2. ?a=10&b=20&a=30 解析查询参数')


# 1.解析 拼接路径的参数   /1999/beijing/
def login_connect(request, city, year):
    print('解析拼接路径的参数----年份:', year)
    print('解析拼接路径的参数----城市:', city)

    return HttpResponse('1.1 10/20/拼接路径参数')


# Create your views here.
def login(request):
    return HttpResponse('1.研究request请求对象 传参  1.1 10/20/拼接路径 1.2 ?a=10&b=20&a=30 1.3 json xml str 1.4 form 1.5 请求头')
