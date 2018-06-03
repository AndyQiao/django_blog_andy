from django.db import models
from blog_andy.models import Article

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    qq = models.CharField(max_length = 128, blank=True)
    text = models.TextField()
    created_time = models.DateTimeField()
    
    article = models.ForeignKey(Article)

    def __str__(selft):
        return '{' + self.text + '}@' + name
