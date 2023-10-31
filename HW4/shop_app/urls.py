from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='main'),
    path('products/', views.products, name='products'),
    path('product/<int:id_product>', views.product, name='product'),
    path('order/<int:id_order>', views.order, name='order'),
    path('clients/', views.clients, name='clients'),
    path('orders/', views.orders, name='orders'),
    path('client_orders/<int:id_client>', views.client_orders, name='client_orders'),
    path('client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted, name='client_products_sorted'),
    path('product_form/<int:id_product>', views.product_form, name='product_form'),


]