import django
import os
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

if __name__ == '__main__':
    print("Starting Rango population script...")
    show_users()
    #del_user('qiaocongAdmin')



