from django.db import models
from ckeditor.fields import RichTextField  # Assuming you are using CKEditor for description_html



class News(models.Model):
    headline = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    description_html = RichTextField(blank=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)


    def __str__(self):
        return self.headline



