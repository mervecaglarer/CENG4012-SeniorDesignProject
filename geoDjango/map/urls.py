from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/<str:date>', views.map, name='map')
]