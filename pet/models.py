from django.contrib.auth.models import User
from django.db import models
from reference.models import RefTypeOfAnimal, RefBreed


class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey(RefTypeOfAnimal, models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    special_notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.CASCADE)

    class Meta:
        db_table = 'pet'


class PetProfile(models.Model):
    breed = models.ForeignKey(RefBreed, models.CASCADE)
    breed_characteristics = models.TextField(blank=True, null=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    scientific_name = models.CharField(max_length=50, blank=True, null=True)
    taxonomy_class = models.CharField(max_length=50, blank=True, null=True)
    conservation_status = models.CharField(max_length=50, blank=True, null=True)
    habitat = models.CharField(max_length=50, blank=True, null=True)
    diet = models.CharField(max_length=50, blank=True, null=True)
    average_lifespan = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=10, blank=True, null=True)
    behavior = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'pet_profile'
