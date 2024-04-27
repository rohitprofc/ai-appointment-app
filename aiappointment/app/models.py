from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # You should hash passwords before storing them
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    zip_code = models.CharField(max_length=6)
