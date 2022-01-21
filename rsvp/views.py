from django.shortcuts import render
from rsvp.registry import get_products


def rsvp(request):
    return render(request, 'rsvp/rsvp.html')


def home(request):
    context = {'products': get_products()}
    return render(request, 'rsvp/home.html', context=context)


def upload_guests(request):
    if request.method == 'POST':
        file = request.FILES['guestlist']

def dashboard(request):
    return render(request,'rsvp/dashboard.html')
    


