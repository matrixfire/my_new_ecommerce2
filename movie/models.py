from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Blog(models.Model):
    title = models.CharField(max_length=100)
    # description = models.CharField(max_length=250)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    
class Review(models.Model):    
    text = models.CharField(max_length=100)    
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Blog,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()    

    def __str__(self):
        return self.text