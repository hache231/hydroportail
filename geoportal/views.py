from django.shortcuts import render
from geoportal.models import station


# Create your views here.
def about(request):
    return render(request, 'about.html')

def map(request):
    stations = station.objects.all()
    return render(request, 'map.html', {'stations': stations})