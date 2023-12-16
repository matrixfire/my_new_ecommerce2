

# from django.db import models
# from ckeditor.fields import RichTextField  # Assuming you are using CKEditor for description_html

# class BlogPost(models.Model):
#     title = models.CharField(max_length=200, blank=True)
#     content = models.TextField(blank=True)
#     description_html = RichTextField(blank=True)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

#     def __str__(self):
#         return self.title



from django.db import models
from ckeditor.fields import RichTextField
# from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    description_html = RichTextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug when saving the object if it doesn't exist
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs:blog_detail', args=[str(self.id), self.slug])