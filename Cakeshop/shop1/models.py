from django.db import models

# Create your models here.
class Cakeshop(models.Model):

    choose_cake = models.CharField(max_length=60)
    shape = models.CharField(max_length=30)
    choose_icing = models.CharField(max_length=60)
    choose_flavors = models.CharField(max_length=60)
    no_of_servings = models.IntegerField()
    any_allergies = models.CharField(max_length=60)
    speacial_request = models.CharField(max_length=120)

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    date_required = models.DateField()
    time_required = models.TimeField()