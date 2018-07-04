import django
import os
from datetime import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from blog_andy.models import Article, Tag, Category
from django.contrib.auth.models import User

def show_users():
    users = User.objects.all()
    for user in users:
        print(user)
def del_user(user_name):
    user = User.objects.get(username=user_name)
    user.delete()
    #user.save()

def show_archives(year, month):
    # post_list = Article.objects.filter(
    #     created_time__year = year,
    #     created_time__month = month).order_by('-created_time')
    post_list = Article.objects.filter(
        created_time = '2018-06-06 09:04:00.000000'
    )
    #post_list=Article.objects.all()
    for post in post_list:
        print(post)

if __name__ == '__main__':
    print("Starting Rango population script...")
    #show_users()
    #del_user('qiaocongAdmin')
    show_archives('2018','5')



def


