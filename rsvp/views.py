from django.shortcuts import render
from rsvp.registry import get_products
from rsvp.guest_io import import_guest_csv
from django.http import *
from rsvp.models import Guest, Response
import json
from django.http import JsonResponse


def rsvp(request):
    guests = [f"{guest.f_name} {guest.s_name}" for guest in Guest.objects.all()]
    guests_json = json.dumps(guests)
    context = {'guests': guests_json}
    return render(request, 'rsvp/rsvp/rsvp.html', context=context)


def home(request):
    # context = {'products': get_products()}
    return render(request, 'rsvp/home/home.html')


def upload_guests(request):
    if request.method == 'POST':
        print(request.FILES)
        file = request.FILES.get('guest-list')
        print(file)
        import_guest_csv(file)
    return HttpResponseRedirect(redirect_to='/dashboard')


def dashboard(request):
    context = {
        'guests': Guest.objects.all(),
        'responses': Response.objects.all()
    }
    return render(request, 'rsvp/dashboard/dashboard.html', context=context)


def guests_json(request):
    guests = Guest.objects.all()
    guest_names = [guest.full_name for guest in guests]

    return JsonResponse(guest_names)



