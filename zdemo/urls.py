"""zdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #     1. 总路由  找  子路由
    url(r'^', include('auser.urls')),


    #     2. 定义了 request的应用
    url(r'^', include('brequest.urls')),

    #     3. 定义 resposne的应用
    url(r'^', include('cresponse.urls')),

    #     4. 操作 cookie的应用
    url(r'^', include('dcookie.urls')),
    #     5. 操作 session的应用
    url(r'^', include('ereview.urls')),
]
