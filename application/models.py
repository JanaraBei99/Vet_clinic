from django.db import models

from pet.models import Pet


class MedRecord(models.Model):
    pet = models.ForeignKey(Pet, models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    clinic_or_vet = models.CharField(max_length=50, blank=True, null=True)
    dosage = models.CharField(max_length=30, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'med_record'
