# filepath: /Users/idris/Documents/hydroportail/geoportal/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('map/', views.map, name='map'),
    path('api/stations/', views.station_data, name='station_data'),
    path('api/stations/<int:pk>/', views.stations_by_sector, name='filterd_station_data'),
    path('api/territories/', views.territories_data_initial, name='territories_data_initial'),
    path('api/territories/<int:pk>/', views.territories_data, name='territories_data'),
    path('api/sectors/', views.territories_data, name='sectors_data_initial'),
    path('api/sectors/<int:pk>/', views.sectors_data, name='sectors_data'),
    path('api/provinces_territories/<int:pk>/', views.province_territories, name='province_territories'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)