# blog/urls.py
from django.urls import path
from .views import blog_list, blog_detail

app_name = 'blogs'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:post_id>/', blog_detail, name='blog_detail'),
]
