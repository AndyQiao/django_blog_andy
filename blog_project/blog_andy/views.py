from django.shortcuts import render, get_object_or_404
from blog_andy.models import Category, Tag, Article
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse

def index1(request):
    output_html = "欢迎访问我的博客首页！"
    all_article = Article.objects.all()
    for article in all_article:
        output_html += "\r\n"
        output_html += article.get_all()
    return HttpResponse(output_html)

def index2(request):
    return render(request, 'blog_andy/index.html', context = {
        'title':'我的博客首页',
        'welcome':'欢迎访问andyQiao的博客首页'
    })

def index(request):
    #all_article = Article.objects.all().order_by('-create_time')
    all_article = Article.objects.all()
    return render(request, 'blog_andy/index.html', context = {
        'post_list':all_article
    })

def detail(request, pk):
    ariticle = get_object_or_404(Article, pk=pk)
    return render(request, 'blog_andy/detail.html', context = {
        'post':ariticle
    })
