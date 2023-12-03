from django.shortcuts import render, redirect
from .models import PropertyProfile
from .models import PropertyUnit
from .models import Features
from .forms import Unit_Fileter_Form


def properties(request):
    property_name = PropertyProfile.objects.all()
    context = {'properties': property_name}
    return render(request, 'property.html', context)

def property_unit(request, pk=None):
    if pk:
        try:
            property_name = PropertyProfile.objects.get(id=pk)
        except Exception:
            return redirect('properties')

        property_features = property_name.features.all()
        features = ', '.join(list(map(lambda x: x.name, property_features)))
        property_units = property_name.unit.all()
        context = {'property': property_name, 'property_units': property_units, 'features': features}        
        return render(request, 'property_unit.html', context)

    property_name = PropertyProfile.objects.all()
    form = Unit_Fileter_Form()
    unit_list = []
    for property in property_name:
        unit = property.unit.all()
        unit_list += unit
    context = {'property_units': unit_list, 'form': form}
    return render(request, 'property_unit.html', context)

def unit_details(request, pk=None):
    if pk:
        try:
            unit = PropertyUnit.objects.get(id=pk)
        except Exception:
            return redirect('properties')
        context = {'unit': unit}
        return render(request, 'unit_detail.html', context)
    return redirect('properties')

def property_search(request):
    if request.method == 'POST':
        feature_name = request.POST['value']
        features = Features.objects.filter(name__icontains=feature_name)
        property_list = []

        for feature in features:
            properties = feature.property.all()
            property_list += properties
        context = {'properties': property_list}
        return render(request, 'property.html', context)
    return redirect('properties')

def search_unit(request):
    form = Unit_Fileter_Form(request.GET or None)
    if form.is_valid():
        interior = request.GET['interior']
        rental_cost = request.GET['rental_cost']
        type = request.GET['type']
        unit_filter = PropertyUnit.objects.filter(
            rental_cost__lt=rental_cost,
            type=type,
            interior=interior
        )
        context = {'property_units': unit_filter, 'form': form}
        return render(request, 'property_unit.html', context)
    return redirect('property_unit_all')
    