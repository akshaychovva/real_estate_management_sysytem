from django.db import models
from property.models import PropertyUnit
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=PropertyUnit)
def create_tenant(sender, instance, created, **kwrgs):
    if created:
        tenant = TenantProfile(property_unit=instance)
        tenant.save()

class TenantProfile(models.Model):
    property_unit = models.OneToOneField('property.PropertyUnit', on_delete=models.SET_NULL, null=True, blank=True)
    tenant_name = models.CharField(max_length=30, default='Nil')
    tenant_address = models.TextField(max_length=100, default='Nil')
    document_proofs = models.TextField(max_length=100, default='Nil')

    agreement_end_date = models.DateField(default='1960-01-01')
    monthly_rent_date = models.TextField(default='1960-01-01')

    def __str__(self) -> str:
        return self.tenant_name