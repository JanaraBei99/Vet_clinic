from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    code = models.CharField(max_length=6)
    code_created_at = models.DateTimeField(default=timezone.now)
    is_used = models.BooleanField(default=False)

    def is_code_expired(self):
        return timezone.now() > self.code_created_at + timedelta(minutes=10)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey("reference.RefRole", on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    preferred_language = models.CharField(max_length=20, blank=True, null=True)
    clinic = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    name_of_organization = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    third_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return f'{self.last_name} {self.last_name}'


class Knowledge(models.Model):
    knowledge = models.TextField(max_length=100)

    class Meta:
        db_table = 'knowledge'

