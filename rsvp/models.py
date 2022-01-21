from django.db import models


# Create your models here.
class Guest(models.Model):
    f_name = models.CharField(max_length=50)
    s_name = models.CharField(max_length=50)



class Response(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE)
    email = models.EmailField()
    datetime = models.DateTimeField()
    can_attend = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    dietary_reqs = models.CharField(max_length=1000)
    note = models.CharField(max_length=1000)
