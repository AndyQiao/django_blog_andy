from django.db import models
from blog_andy.models import Article

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=256, blank=True)
    qq = models.CharField(max_length = 128, blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(selft):
        return '{' + self.text + '}@' + name
