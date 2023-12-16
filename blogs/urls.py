# blog/urls.py
from django.urls import path
from .views import blog_list, blog_detail

app_name = 'blogs'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    # path('<int:post_id>/', blog_detail, name='blog_detail'),
    path('<int:post_id>/<slug:slug>/', blog_detail, name='blog_detail'),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
