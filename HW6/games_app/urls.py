from django.urls import path
from . import views

urlpatterns = [
    path('eagle/', views.eagle, name='eagle'),
    path('cube/', views.cube, name='cube'),
    path('random_number/', views.random_number, name='random_number'),
    path('show_elements/<int:n>', views.show_elements, name='show_elements'),
    path('eagle_tmpl/<int:count>', views.eagle_tmpl, name='eagle_tmpl'),
]
