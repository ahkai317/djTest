# article/urls.py

from django.urls import path
from appTest import views

app_name = 'article' #0416 這邊可以改成appTest嗎? 目前進度改沒bug

urlpatterns = [
    path('', views.article_list, name='list'),

    #0416 Class-View
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]