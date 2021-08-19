from django.contrib import admin
from .models import *
# Register your models here.


class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','email', ) #visualizar columnas



admin.site.register(Signup, SignupAdmin)