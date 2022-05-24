from django.shortcuts import render
from .forms import VehicleForm
from django.http import HttpResponse
from .models import Vehicle


# Create your views here.
def home(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Vehicle Created")
    form = VehicleForm()
    vehicles = Vehicle.objects.all()
    context = {
        "form": form,
        "vehicles": vehicles
    }
    return render(request, "home.html", context)
