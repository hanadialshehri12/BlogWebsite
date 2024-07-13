from django.db import models

class User(models.Model):
  username = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.username} {self.email}"

class Category(models.Model):
  nameCat=models.CharField(max_length=150)
  def __str__(self):
    return f"{self.nameCat}"

class Post(models.Model):
  titlePos = models.CharField(max_length=150)
  contentPos =models.TextField(default="")
  categoryPos=models.ForeignKey(Category,on_delete=models.CASCADE)
  DatePublished = models.DateField()
  def __str__(self):
    return f"{self.titlePos} {self.contentPos} {self.categoryPos} {self.DatePublished}"



class Comment(models.Model):
  postID = models.ForeignKey(Post,on_delete=models.CASCADE)
  userID = models.ForeignKey(User, on_delete=models.CASCADE)
  contentCom = models.TextField(default="")
  DatePosted = models.DateField()

  def __str__(self):
    return f"{self.postID} {self.userID} {self.contentCom} "
