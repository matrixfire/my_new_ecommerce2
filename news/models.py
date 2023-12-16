from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# class News(models.Model):
#     headline = models.CharField(max_length=200, blank=True)
#     body = models.TextField(blank=True)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     description_html = RichTextField(blank=True)
#     image = models.ImageField(upload_to='news_images/', null=True, blank=True)


#     def __str__(self):
#         return self.headline


from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class News(models.Model):
    headline = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    description_html = RichTextField(blank=True)
<<<<<<< HEAD
    image = models.ImageField(upload_to='news_images/', null=True, blank=True,  default='blog/images/base-cob-led-2.jpg')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # If headline is not provided, set a default value
        if not self.body:
            self.body = "COB Led"
        
        # If slug is not provided, generate one from the headline
        if not self.slug:
            self.slug = slugify(self.headline)

        super().save(*args, **kwargs)

=======
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
>>>>>>> 50b1b29bb0bcbb00ba2d7f9facceb7811a74a4e5

    def __str__(self):
        return self.headline

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id), self.slug])
=======
    def save(self, *args, **kwargs):
        # Auto-generate slug from the headline if not provided
        if not self.slug:
            self.slug = slugify(self.headline)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.slug)])


>>>>>>> 50b1b29bb0bcbb00ba2d7f9facceb7811a74a4e5
