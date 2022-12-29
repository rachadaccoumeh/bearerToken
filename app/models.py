import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Location(models.Model):
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address

    @property
    def abr_location(self):
        return self.city + "/" + self.country


# location = Location(city="city", zip="zip", state="state", country="country", address="address")
# location.save()


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Admission(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients1")
    time = models.TimeField(default=timezone.now)  # datetime.date.now()
    date = models.DateField(default=timezone.now)  # datetime.date.today()
    reason = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class MedicalInfo(models.Model):
    BLOOD = (
        ('A+', 'A+ Type'),
        ('B+', 'B+ Type'),
        ('AB+', 'AB+ Type'),
        ('O+', 'O+ Type'),
        ('A-', 'A- Type'),
        ('B-', 'B- Type'),
        ('AB-', 'AB- Type'),
        ('O-', 'O- Type'),
    )

    @staticmethod
    def toBlood(key):
        for item in MedicalInfo.BLOOD:
            if item[0] == key:
                return item[1]
        return "None"

    patient = models.ForeignKey(User, related_name="patiento", on_delete=models.CASCADE)
    bloodType = models.CharField(max_length=10, choices=BLOOD)
    allergy = models.CharField(max_length=100)
    alzheimer = models.BooleanField()
    asthma = models.BooleanField()
    diabetes = models.BooleanField()
    stroke = models.BooleanField()
    comments = models.CharField(max_length=700)


class MedicalTest(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    doctor = models.ForeignKey(User, related_name="docs", on_delete=models.PROTECT)
    patient = models.ForeignKey(User, related_name="pts", on_delete=models.CASCADE)
    private = models.BooleanField(default=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.name


class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=32)
    verified = models.BooleanField(default=False)


class PhoneVerification(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    verification_code = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
