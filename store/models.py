from django.db import models
from django.urls import reverse
from django.utils import timezone
from pathlib import Path
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            return reverse('store:product_list_by_category', args=[self.slug])
        except:
            return 'some_url'

class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='uploads/products/', blank=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        # Update last_modified_field whenever the model is saved
        self.updated = timezone.now()
        super().save(*args, **kwargs)



class Carousel(models.Model):
    # image       = models.ImageField(upload_to="pics/%y/%m/%d/")
    image       = models.ImageField(upload_to="pics/")
    title       = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title



class HTML_DIY(models.Model):
    name = models.CharField(max_length=150)
    html_content = RichTextField(blank=True)

    def __str__(self):
        return self.name


def read_html_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ''
    except Exception as e:
        print(f"Error reading file: {e}")
        return ''
