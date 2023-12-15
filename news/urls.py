from django.urls import path
from . import views

app_name = "news"
urlpatterns = [    
    path('', views.news, name='news'),
    path('load-more-news/', views.load_more_news, name='load_more_news'),
    path('<int:news_id>/', views.news_detail, name='news_detail'),
]
