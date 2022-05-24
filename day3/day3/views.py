from django.shortcuts import render


def home(request, temperature_user):
    temperature = temperature_user
    context = {
        "temperature": temperature
    }
    return render(request, "home.html", context)
