# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blog/', views.blog, name='blog'),
    path('blog/blogs/', views.blogs, name='blogs'),
    path('blog/categories/', views.categories, name='categories'),
    path('blog/comments/', views.comments, name='comments'),
    path('blog/blogs/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),


]
