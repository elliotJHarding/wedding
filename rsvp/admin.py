from django.contrib import admin
from rsvp.models import Guest
# Register your models here.


class GuestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Guest, GuestAdmin)
