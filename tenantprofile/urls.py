from django.urls import path
from . import views

app_name = 'tenants_names'

urlpatterns = [
    path('<int:pk>', views.tenant_profile, name='tenant_profile'),
    path('', views.tenants, name='tenants')
]
