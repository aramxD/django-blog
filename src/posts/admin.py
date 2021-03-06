from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', ) #visualizar columnas

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', ) #visualizar columnas


class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'timestamp') 


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user', ) #visualizar columnas


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostView, PostViewAdmin)
admin.site.register(Comment, CommentAdmin)