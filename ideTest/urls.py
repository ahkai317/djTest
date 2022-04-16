"""ideTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from appTest import views
# from article import views

# app_name = 'article' #0410 DRF #0414 好像不需要(之後要測試全部整合進專案的url)

urlpatterns = [
    path('admin/', admin.site.urls),

    # When enter xxx/index/ -> exec function
    path('', views.index),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),

    path('orm/', views.orm),

    path('tpl/', views.tpl),
    path('news/', views.news),

    path('something/', views.something),
    path('login/', views.login),

    # project: membership administration
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete),
    # path('info/delete/', views.info_delete),


    # ======================================================================
    # 0410 DRF前置補充
    # path('article-list/', views.article_list, name='article_list'),
    # ======================================================================
    # 0410 DRF
    # drf_vue_blog/urls.py
    path('api-auth/', include('rest_framework.urls')),
    path('api/article/', include('appTest.urls', namespace='article')),

]

