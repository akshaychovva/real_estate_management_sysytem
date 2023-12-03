from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('property_unit/<int:pk>', views.property_unit, name='property_unit'),
    path('property_unit/', views.property_unit, name='property_unit_all'),
    path('unit_details/<int:pk>', views.unit_details, name='unit_details'),
    path('property_search', views.property_search, name='property_search'),
    path('search_unit', views.search_unit, name='search_unit')
]
