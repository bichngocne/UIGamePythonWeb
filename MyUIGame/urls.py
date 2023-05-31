from django.urls import path
from .import views
urlpatterns = [
    path('index', views.index, name="index"),
    path('weapons', views.get_all_weapon, name='weapons'),
    path('figures', views.get_figure, name='figures'),
]