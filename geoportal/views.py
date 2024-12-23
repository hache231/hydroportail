# filepath: /Users/idris/Documents/hydroportail/geoportal/views.py
from django.shortcuts import render
from geoportal.models import station, provinces, territories, sectors
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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
    station_list = list(stations.values('name', 'owner', 'physical_adresse','latitude', 'longitude', 'type_id', 'state', 'storage_capacity', 'opening_hours', 'closing_hours', 'province_id', 'territory_id', 'sector_id'))
    return JsonResponse(station_list, safe=False)

@login_required(login_url='/login/')
def stations_by_sector(request, pk):
    stations = station.objects.filter(sector_id=pk)
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id', 'state', 'storage_capacity', 'opening_hours', 'closing_hours', 'province_id', 'territory_id', 'sector_id'))
    return JsonResponse(station_list, safe=False)

@login_required(login_url='/login/')
def stations_by_territories(request, pk):
    stations = station.objects.filter(territory_id=pk)
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id', 'state', 'storage_capacity', 'opening_hours', 'closing_hours', 'province_id', 'territory_id', 'sector_id'))
    return JsonResponse(station_list, safe=False)

@login_required(login_url='/login/')
def stations_by_provinces(request, pk):
    stations = station.objects.filter(province_id=pk)
    station_list = list(stations.values('name', 'owner', 'latitude', 'longitude', 'type_id', 'state', 'storage_capacity', 'opening_hours', 'closing_hours', 'province_id', 'territory_id', 'sector_id'))
    return JsonResponse(station_list, safe=False)

@login_required(login_url='/login/')
def territories_data_initial(request):
    territories_list = territories.objects.all()
    territories_data = list(territories_list.values('id', 'territory_name'))

    sectors_data = []
    for territory in territories_list:
        sectors_list = sectors.objects.filter(territory_id=territory.id)
        sectors_data.extend(list(sectors_list.values('id', 'sector_name', 'territory_id')))
    
    response_data = {
        'territories': territories_data,
        'sectors': sectors_data
    }
    return JsonResponse(response_data, safe=False)

@login_required(login_url='/login/')
def territories_data(request, pk):
    territories_list = territories.objects.filter(province_id=pk)
    territories_data = list(territories_list.values('id', 'territory_name'))
    
    sectors_data = []
    for territory in territories_list:
        sectors_list = sectors.objects.filter(territory_id=territory.id)
        sectors_data.extend(list(sectors_list.values('id', 'sector_name', 'territory_id')))
    
    response_data = {
        'territories': territories_data,
        'sectors': sectors_data
    }
    
    return JsonResponse(response_data, safe=False)


@login_required(login_url='/login/')
def sectors_data(request, pk):
    sectors_list = sectors.objects.filter(territory_id=pk)
    sectors_data = list(sectors_list.values('id', 'sector_name'))

    province_list = provinces.objects.filter(id=territories.objects.get(id=pk).province_id)
    province = list(province_list.values('id', 'province_name'))

    response_data = {
        'sectors': sectors_data,
        'province': province
    }
    
    return JsonResponse(response_data, safe=False)


def province_territories(request, pk):
    territories_list = territories.objects.filter(id=sectors.objects.get(id=pk).territory_id)
    territories_data = list(territories_list.values('id', 'territory_name'))

    provinces_data = []
    for territory in territories_list:
        provinces_list = provinces.objects.filter(id = territory.province_id)
        provinces_data.extend(list(provinces_list.values('id', 'province_name')))
    
    response_data = {
        'territories': territories_data,
        'provinces': provinces_data
    }
    return JsonResponse(response_data, safe=False)
