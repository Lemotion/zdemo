from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def custom_response(request):
    # return HttpResponse('操作 响应对象')

    #  1.操作 参数
    #     return HttpResponse(
    # content="浏览器显示的内容",
    # 内容的类型
    # content_type='',
    # 状态码
    # status=202
    # )


    # 2. 操作 属性

    response = HttpResponse()
    response.content = '操作 属性'
    response.status_code = 200

    return response