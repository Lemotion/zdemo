from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def session_response(request):
    #1.设置Session
    #redis保存的Session类型是string字符串
    # 1.给浏览器设置了cookies的值 sessionid
    # 2.将name 储存到redis里面
    request.session['name'] ='ITHEIMA'
    request.session['gender'] = '666'
    # 2.取出session值
    print('取出session值：', request.session['name'])
    # 3.清除session，清除制定的key键
    request.session.clear()
    return HttpResponse('操作Session')