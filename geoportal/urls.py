from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('map/', views.map, name='map'),
    path('api/stations/', views.station_data, name='station_data'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


