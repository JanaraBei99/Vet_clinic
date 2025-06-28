from django.contrib import admin
from .models import ArticleView
# Register your models here.

@admin.register(ArticleView)
class ArticleViewAdmin(admin.ModelAdmin):
    pass
