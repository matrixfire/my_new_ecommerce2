# blogs/admin.py
from django.contrib import admin
from .models import BlogPost

# admin.site.register(BlogPost)



# admin.py
from django.contrib import admin
from .models import BlogPost
from django.utils.text import slugify

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)