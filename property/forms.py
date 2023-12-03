from django import forms
from.models import PropertyUnit

class Unit_Fileter_Form(forms.ModelForm):

    class Meta:
        model = PropertyUnit
        exclude = ['property_profile', 'unit_code']