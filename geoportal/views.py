from django.shortcuts import render
from geoportal.models import station
from django.http import JsonResponse

# Create your views here.
def about(request):
    return render(request, 'about.html')

def map(request):
    return render(request, 'carte.html')

def station_data(request):
    stations = station.objects.all()
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id','state', 'Storage_capacity', 'Opening_hours', 'closing_hours'))
    return JsonResponse(station_list, safe=False)

