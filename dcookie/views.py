from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_cookie(request):

    #1.设置Cookie 1.验证身份 2. 保持会话
    response = HttpResponse('操作Cookie')
    #HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
    response.set_cookie('itcast','itheima',max_age=30)
    #获取cookie 进行验证
    print(request.COOKIES)
    print(type(request.COOKIES['itcast']))
    return response