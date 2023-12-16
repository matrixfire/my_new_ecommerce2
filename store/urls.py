from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
<<<<<<< HEAD
from .views import RobotsTxtView
from . import views



app_name = 'store'

=======
from . import views
from .views import RobotsTxtView
from .sitemaps import YourModelSitemap

sitemaps = {
    'your_model': YourModelSitemap,
}

app_name = 'store'
>>>>>>> 50b1b29bb0bcbb00ba2d7f9facceb7811a74a4e5
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
<<<<<<< HEAD
=======
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemaps'),
>>>>>>> 50b1b29bb0bcbb00ba2d7f9facceb7811a74a4e5
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
]
