from django.shortcuts import render
from django.contrib.auth.models import User, auth
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
    return render(request, 'weapons.html', {'weapons': weapons, 'weapon_types': weapon_types})


def get_figure(request):
    figure_list = figure_model.objects.select_related('attribute').all()
    attributes = attribute_model.objects.all()
    return render(request, 'figure.html', {'figures': figure_list, 'attributes': attributes})

def get_territory(request):
    territories = territory_model.objects.all()
    return render(request, 'territory.html', {'territories': territories})

def get_figure_detail(request,id):
    figure_detail = figure_model.objects.select_related('attribute', 'gender', 'territory').filter(id=id)
    # Kiểm tra xem đối tượng Figure có tồn tại không
    if figure_detail.exists():
        figure = figure_detail.first()
        attribute = figure.attribute
        gender = figure.gender
        territory = figure.territory
    return render(request, 'figuredetail.html',{'figure':figure,'pk':id})

def get_weapon_detail(request,id):
    weapon_detail = weapon_model.objects.select_related('weapone_type').filter(id=id)
    # Kiểm tra xem đối tượng Figure có tồn tại không
    if weapon_detail.exists():
        weapon = weapon_detail.first()
    return render(request, 'weapondetail.html',{'weapon':weapon,'pk':id})

def login(request):
    return render(request,'login.html');


def logout(request):
    auth.logout(request)
    return redirect('/')