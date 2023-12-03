from django.shortcuts import render
from .models import TenantProfile

def tenant_profile(request, pk=None):
    if pk:
        try:
            tenant = TenantProfile.objects.get(id=pk)
        except Exception:
            raise ValueError
        context = {'tenant': tenant}
        return render(request, 'tenantprofile.html', context)
    
def tenants(request):
    tenants = TenantProfile.objects.exclude(tenant_name='Nil')
    context = {'tenants': tenants}
    return render(request, 'tenants.html', context)
