import markdown
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
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body,
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])
    return render(request, 'blog_andy/detail.html', context = {
        'post':article
    })

def archives(request, year, month):
    articles = Article.objects.filter(
        created_time__year = year,
        created_time__month = month).order_by('-created_time')
    return render(request, 'blog_andy/index.html', context = {
        'post_list':articles
    })

def categories(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog_andy/index.html', context={
        'post_list':post_list
    })