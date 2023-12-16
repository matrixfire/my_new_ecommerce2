from django.db import models
from ckeditor.fields import RichTextField  # Assuming you are using CKEditor for description_html



# class News(models.Model):
#     headline = models.CharField(max_length=200, blank=True)
#     body = models.TextField(blank=True)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     description_html = RichTextField(blank=True)
#     image = models.ImageField(upload_to='news_images/', null=True, blank=True)


#     def __str__(self):
#         return self.headline



from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class News(models.Model):
    headline = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    description_html = RichTextField(blank=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto-generate the slug when saving the News instance
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.headline
