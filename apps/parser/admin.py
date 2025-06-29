from django.contrib import admin
from .models import Parsing
# Register your models here.

@admin.register(Parsing)
class ParsingAdmin(admin.ModelAdmin):
    pass
