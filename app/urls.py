from django.urls import path
from .views import home, tir,plot

urlpatterns = [
    path('', home,name='home'),
    path('tir', tir,name='tir'),
    path('plot', plot,name='plot'),
]