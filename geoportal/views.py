from django.shortcuts import render
from geoportal.models import station
from django.http import JsonResponse

# Create your views here.
def about(request):
    return render(request, 'about.html')

def map(request):
    stations = station.objects.all()
    return render(request, 'map.html', {'stations': stations})

def station_data(request):
    stations = station.objects.all()
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id'))
    return JsonResponse(station_list, safe=False)