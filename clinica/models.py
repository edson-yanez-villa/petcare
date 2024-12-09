from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"


class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    medical_history = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def clean(self):
        if self.age < 0:
            raise ValidationError("Pet age cannot be negative.")


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()
    veterinarian = models.CharField(max_length=100)

    def clean(self):
        if Appointment.objects.filter(pet=self.pet, date_time=self.date_time).exists():
            raise ValidationError(
                "An appointment already exists for this pet at this time."
            )


class Treatment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medication = models.TextField()
    treatment_date = models.DateField()

    def __str__(self):
        return f"Treatment for {self.pet.name} - {self.treatment_date}"
