from django.shortcuts import render
from geoportal.models import station, provinces, territories, sectors
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def map(request):
    provinces_list = provinces.objects.all()
    territories_list = territories.objects.all()
    sectors_list = sectors.objects.all()
    return render(request, 'carte.html', {'provinces': provinces_list, 'territories': territories_list, 'sectors': sectors_list})


@login_required(login_url='/login/')
def station_data(request):
    stations = station.objects.all()
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id', 'state', 'storage_capacity', 'opening_hours', 'closing_hours', 'province_id', 'territory_id', 'sector_id'))
    return JsonResponse(station_list, safe=False)

@login_required(login_url='/login/')
def stations_by_sector(request, pk):
    stations = station.objects.filter(sector_id=pk)
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id', 'state', 'storage_capacity', 'opening_hours', 'closing_hours', 'province_id', 'territory_id', 'sector_id'))
    return JsonResponse(station_list, safe=False)
