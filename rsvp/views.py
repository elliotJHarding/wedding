from django.shortcuts import render
from django.template.loader import render_to_string
from rsvp.registry import get_products
from rsvp.guest_io import import_guest_csv
from django.http import *
from rsvp.models import Guest, Response
import json
from django.http import JsonResponse
from django.core.mail import send_mail


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


def thanks(request, guest_id):
    context = {'guest': Guest.objects.filter(id=guest_id)}

    return render(request, 'rsvp/rsvp/thanks.html', context)


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

        attend = data.get('attend', None)
        veg = data.get('veg', None)

        if attend == 'yes':
            response.can_attend = True
        elif attend == 'no':
            response.can_attend = False

        if response.can_attend:
            if veg == "yes":
                response.vegetarian = True
            elif veg == 'no':
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
            guest.email = response.email
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
        context = {'diet': response.dietary_reqs, 'note': response.note, 'veg': response.note, 'attend': response.can_attend}
        send_mail(
            subject='Thanks for Responding',
            message='Thankyou for Responding',
            from_email='info@elliotandemmawedding.com',
            recipient_list=[response.email],
            html_message=render_to_string('templates/rsvp/emails/response.html', context=context)

        )
        send_mail(
            subject=f"{Guest.full_name} responded",
            message=f"{Guest.full_name}, attending: {Guest.attending}, veg: {Guest.vegetarian}, email: {Guest.email}",
            from_email='info@elliotandemmawedding.com',
            recipient_list=['elliotandemmawedding@gmail.com'],
            html_message=render_to_string('templates/rsvp/emails/response_info.html')
        )

    return JsonResponse({'id': guest.id})


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



