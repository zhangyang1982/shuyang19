"""datalist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),     #后台
    path('',include('first.urls'), name="first"),      #首页
    path('user/', include('user.urls')),#用户管理
    path('sscCq/',include('sscCq.urls')),#重庆
    path('sscXj/',include('sscXj.urls')),#新疆
    path('sscTj/',include('sscTj.urls')),#天津
    path('sscHn/',include('sscHn.urls')),#河内彩
    path('gd11x5/',include('gd11x5.urls')),#广东11选5
    path('bjpk10/',include('bjpk10.urls')),#北京PK10
    path('Azxy10/',include('Azxy10.urls')),#澳洲幸运10
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')), #网站图标

]
