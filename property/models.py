from django.db import models



class PropertyProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    location = models.CharField(max_length=100)
    features = models.ManyToManyField('Features',related_name='property', blank=True)

    def __str__(self) -> str:
        return self.name
    

class PropertyUnit(models.Model):
    property_profile = models.ForeignKey('PropertyProfile', related_name='unit', on_delete=models.CASCADE)
    unit_code = models.CharField(max_length=10)
    interior_choices = [
        ('Not Furnished', 'Not Furnished'),
        ('Semi Furnished', 'Semi Furnished'),
        ('Fully Furnished', 'Fully Furnished')
    ]
    rental_cost = models.FloatField(max_length=30)
    interior = models.CharField(max_length=20, choices=interior_choices)
    type_choices = [
        ('1 BHK', '1 BHK'),
        ('2 BHK', '2 BHK'),
        ('3 BHK', '3 BHK'),
        ('4 BHK', '4 BHK'),
    ]
    type = models.CharField(max_length=5,choices=type_choices)

    def __str__(self) -> str:
        return self.unit_code


class Features(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name