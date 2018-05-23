from django.contrib import admin
from blog_andy.models import Article, Tag, Category

# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)