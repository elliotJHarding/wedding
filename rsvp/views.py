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


def has_plus_one(request):
    if request.method == 'POST':
        guest_name = request.POST.get('guest-name')
        guest = Guest.objects.filter(full_name=guest_name)[0]
        data = {'has_plus1': guest.has_plus1}

        return JsonResponse(data)


def submit_rsvp(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        response = Response()
        guest = Guest.objects.filter(full_name=data.get('guest-name'))[0]

        response.guest = guest


        attend_yes = data.get('attend-yes', None)
        attend_no = data.get('attend-no', None)
        veg_yes = data.get('veg-yes', None)
        veg_no = data.get('veg-no', None)

        if attend_yes == 'on' and attend_no is None:
            response.can_attend = True
        elif attend_yes is None and attend_no == 'on':
            response.can_attend = False

        if response.can_attend:
            if veg_yes == 'on' and veg_no is None:
                response.vegetarian = True
            elif veg_yes is None and veg_no == 'on':
                response.vegetarian = False

            response.email = data.get('email')
            response.dietary_reqs = data.get('diet')
            response.note = data.get('note')

        response.save()

        guest.responded = True

        guest.attending = response.can_attend
        if response.can_attend:
            guest.vegetarian = response.vegetarian
            guest.dietary_reqs = response.dietary_reqs
        guest.save()

        if guest.has_plus1:
            plus_one_name = data.get('plus-one-name')
            f_name, s_name = plus_one_name.split(' ', 1)
            if plus_one_name is not None:
                if guest.added_plus1:
                    # TODO
                    pass
                else:

                    Guest.objects.get_or_create(
                        f_name=f_name,
                        s_name=s_name,
                        full_name=plus_one_name
                    )
                    guest.added_plus1 = True




    return HttpResponse()


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



