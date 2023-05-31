from django.shortcuts import render
from .models import Figure as figure_model
from .models import Weapone as weapon_model
from .models import Weapone_type as weapon_type_model
from .models import Territory as territory_model
from .models import Attribute as attribute_model
# Create your views here.


def index(request):
    figure_list = figure_model.objects.select_related('territory').all()
    territory_list = territory_model.objects.all()
    return render(request, 'index.html', {'figures': figure_list, 'territories': territory_list})


def get_all_weapon(request):
    weapons = weapon_model.objects.select_related("weapone_type").all()
    weapon_types = weapon_type_model.objects.all()
    return render(request, 'weapons.html',{'weapons': weapons, 'weapon_types': weapon_types})
def get_figure(request):
    figure_list = figure_model.objects.select_related('attribute').all()
    attributes = attribute_model.objects.all()
    return render(request, 'figure.html', {'figures': figure_list, 'attributes': attributes})