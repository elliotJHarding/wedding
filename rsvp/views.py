from django.shortcuts import render
from rsvp.registry import get_products
from rsvp.guest_io import import_guest_csv
from django.http import *
from rsvp.models import Guest


def rsvp(request):
    return render(request, 'rsvp/rsvp/rsvp.html')


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
    context= {'guests': Guest.objects.all()}
    return render(request, 'rsvp/dashboard/dashboard.html', context=context)
    


