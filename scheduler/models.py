from django.db import models
from django.core.validators import RegexValidator

# Create your models here.




class customer(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    cno = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),]
    )
    service = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()


class Appointment(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    service = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()


class feedback(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

