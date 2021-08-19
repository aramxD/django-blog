from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    
    path('blog', blog, name='blog'),
    path('search', search, name='search'),
    path('post/<post_id>', post, name='post'),
    ]