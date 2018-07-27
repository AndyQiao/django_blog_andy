import markdown
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Category, Tag, Article
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(ListView):
    model= Article
    template_name = 'blog_andy/index.html'
    context_object_name = 'post_list'

# def index(request):
#     all_article = Article.objects.all()
#     return render(request, 'blog_andy/index.html', context = {
#         'post_list':all_article
#     })

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog_andy/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        #首先获得article对象
        reponse = super(ArticleDetailView, self).get(request, *args, **kwargs)

        #浏览量+1
        self.object.increase_views()

        return reponse

    def get_object(self, queryset=None):
        post = super(ArticleDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        
        form = CommentForm()

        comment_list = self.object.comment_set.all()

        context.update({
            'form':form,
            'comment_list':comment_list
        })

        return context

    

# def detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)

#     # 浏览量+1
#     article.increase_views()

#     # 正文markdown处理
#     article.body = markdown.markdown(article.body,
#                                     extensions=[
#                                         'markdown.extensions.extra',
#                                         'markdown.extensions.codehilite',
#                                         'markdown.extensions.toc',
#                                     ])

#     form = CommentForm()

#     comment_list = article.comment_set.all()

#     context = {
#         'post':article,
#         'form':form,
#         'comment_list':comment_list
#     }

#     return render(request, 'blog_andy/detail.html', context = context)

class ArchivesView(IndexView):
    def get_queryset(self):
        return super(ArchivesView, self).get_queryset().filter(
            created_time__year = self.kwargs.get('year'),
            created_time__month = self.kwargs.get('month')
        )


# def archives(request, year, month):
#     articles = Article.objects.filter(
#         created_time__year = year,
#         created_time__month = month)
#     return render(request, 'blog_andy/index.html', context = {
#         'post_list':articles
#     })

class CategoriesView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return super(CategoriesView, self).get_queryset().filter(category=cate)

# def categories(request, pk):
#     cate = get_object_or_404(Category, pk = pk)
#     post_list = Article.objects.filter(category=cate)
#     return render(request, 'blog_andy/index.html', context={
#         'post_list':post_list
#     })