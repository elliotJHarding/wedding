from django.shortcuts import render

def rsvp(request):
    return render(request, 'rsvp/rsvp.html')

# Create your views here.
