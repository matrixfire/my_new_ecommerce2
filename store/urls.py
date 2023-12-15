from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .views import RobotsTxtView
from .sitemaps import YourModelSitemap

sitemaps = {
    'your_model': YourModelSitemap,
}

app_name = 'store'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemaps'),
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
]
