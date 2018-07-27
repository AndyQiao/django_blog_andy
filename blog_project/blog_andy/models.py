# coding: utf-8

import markdown
from django.utils.html import strip_tags
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Article(models.Model):
    # 标题 & 子标题
    title = models.CharField(max_length=64)
    sub_title =  models.CharField(max_length=64, blank=True)

    # 摘要
    excerpt = models.CharField(max_length=200, blank=True)

    #正文
    body = models.TextField()

    # 创建时间 & 最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 分类 & 标签
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tag, blank = True)

    # 作者
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 浏览量
    views = models.PositiveIntegerField(default=0) 

    def get_all(self):
        output_string = "Title:" + self.title + "_" + self.sub_title + "\n"
        output_string += ("body:"+ self.body + "\n")
        return output_string
    
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + '_' + self.sub_title

    def get_absolute_url(self):
        return reverse('blog_andy:detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


