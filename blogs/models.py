from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    description_html = RichTextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', args=[str(self.slug)])
