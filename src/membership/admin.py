from django.contrib import admin
from .models import *
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','user', ) #visualizar columnas

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','user', ) #visualizar columnas




admin.site.register(Author, AuthorAdmin)
admin.site.register(Member, MemberAdmin)