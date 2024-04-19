from django.urls import path
from . import views

urlpatterns = [
    path('add_client/', views.add_client, name='add_client'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_order/', views.add_order, name='add_order'),
    path('products/', views.products, name='products'),
]
