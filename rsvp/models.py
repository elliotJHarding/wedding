from django.db import models


# Create your models here.
class Guest(models.Model):
    f_name = models.CharField(max_length=50)
    s_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, default="")
    has_plus1 = models.BooleanField(default=False)
    added_plus1 = models.BooleanField(default=False)
    email = models.CharField(max_length=100, default="")
    responded = models.BooleanField(default=False)
    attending = models.BooleanField(default=None, null=True)
    vegetarian = models.BooleanField(default=None, null=True)
    dietary_reqs = models.CharField(max_length=1000, null=True)


class Response(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE)
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)
    can_attend = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    dietary_reqs = models.CharField(max_length=1000)
    note = models.CharField(max_length=1000)
