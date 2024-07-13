from django.contrib import admin
from .models import User,Category,Post,Comment

class UserAdmin(admin.ModelAdmin):
  list_display = ("username", "email",)
admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("nameCat",)
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
  list_display = ("titlePos", "contentPos", "categoryPos", "DatePublished",)
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
  list_display = ("postID", "userID", "contentCom", )
admin.site.register(Comment, CommentAdmin)