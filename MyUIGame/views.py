from django.shortcuts import render
from .models import Figure as figure_model
from .models import Territory as territory_model
# Create your views here.


def index(request):
    territory_list = territory_model.objects.filter();
    figure_list_territory = figure_model.objects.filter(territory=1).select_related("territory").all()
    figure_list_territory1 = figure_model.objects.filter(territory=2).select_related("territory").all()
    figure_list_territory2 = figure_model.objects.filter(territory=3).select_related("territory").all()
    figure_list_territory3 = figure_model.objects.filter(territory=4).select_related("territory").all()
    return render(request, 'index.html', {'territory_list':territory_list,'datas': figure_list_territory,'datas1': figure_list_territory1,'datas2': figure_list_territory2,'datas3': figure_list_territory3})
