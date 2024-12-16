from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('map/', views.map, name='map'),
    path('api/stations/', views.station_data, name='station_data'),
]


