# news/admin.py
from django.contrib import admin
from .models import News
from django.utils.text import slugify

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline',)}

admin.site.register(News, NewsAdmin)
