# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('checkout/', views.checkout, name='checkout'),
    path('receipt/<int:order_id>/', views.receipt, name='receipt'),
]
