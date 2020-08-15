from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    images= models.ImageField(blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.post.title