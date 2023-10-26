from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('order/<int:id_order>', views.order, name='order'),
    path('clients/', views.clients, name='clients'),
    path('orders/', views.orders, name='orders'),

]