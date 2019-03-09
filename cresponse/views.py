from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render


# Create your views here.

# 操作 jsonresponse
# 1.content_type = 'application/json
# 2. json_dict => json_str
def response_json(request):
    # dict_data = {
    #     'a': 1,
    #     "b": 2
    # }

    list_data = [
        {
            'a': 1,
            "b": 2
        }
    ]
    # 1.默认 只接受 dict
    # 2. list_json  需要设置 safe=False 可以传list
    return JsonResponse(list_data, safe=False)


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
    response.status_code = HttpResponseBadRequest.status_code

    return response
