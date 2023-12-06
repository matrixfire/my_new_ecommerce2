from django.contrib import admin
from django.urls import path

from . import views

app_name = 'store'

# urlpatterns = [
#     # path('', views.Index.as_view(), name='homepage'),
#     # path('products', views.ProductsFilter.as_view(), name='products'),
#     path('', views.home_page, name='home_page'),

#     path('products', views.store, name='store'),


#     path('signup', views.Signup.as_view(), name='signup'),
#     path('login', views.Login.as_view(), name='login'),
#     path('logout', views.logout, name='logout'),
#     path('cart', views.auth_middleware(views.Cart.as_view()), name='cart'),
#     path('check-out', views.CheckOut.as_view(), name='checkout'),
#     path('orders', views.auth_middleware(views.OrderView.as_view()), name='orders'),
#     path('detail/<int:product_id>', views.ProductDetail.as_view(), name='detail'),
# ]



urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
