from django.http import HttpResponse
from django.template import loader
from .models import User,Post,Category,Comment

def blog(request):
  myusers = User.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))


def blogs(request):
  myblogs = Post.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
    'myblogs': myblogs,
  }
  return HttpResponse(template.render(context, request))


def categories(request):
  mycategory = Category.objects.all().values()
  template = loader.get_template('categories.html')
  context = {
    'mycategory': mycategory,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def comments(request):
  mycomment = Comment.objects.all().values('postID','contentCom')
  template = loader.get_template('comments.html')
  context = {
    'mycomment': mycomment,

  }
  return HttpResponse(template.render(context, request))

def blogdetails(request,id):
  myblogdetails = Post.objects.get(id=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'myblogdetails': myblogdetails,
  }
  return HttpResponse(template.render(context, request))