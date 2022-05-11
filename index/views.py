from django.shortcuts import render
from django.http import JsonResponse
from .models import Pressure


def index(request):
    pressure = Pressure.objects.all()
    return render(request, "app/index.html", {"pressures": pressure})


def simple_fetch(request):
    pressure = Pressure.objects.all()
    pressure_data = []
    for i in range(len(pressure)):
        pressure_data.append(pressure_to_dict(pressure[i]))

    return JsonResponse({"pressures": pressure_data})


def pressure_to_dict(pressure):
    output = {'uuid': pressure.id, 'pressure': pressure.pressure}

    return output
