from django.db.models.aggregates import Count

from django import template
from blog_andy.models import Article, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Article.objects.all()[:num]

@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt = 0)


