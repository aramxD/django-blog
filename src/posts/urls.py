from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    
    path('blog', blog, name='blog'),
    path('search', search, name='search'),
    path('post/<post_id>', post, name='post'),
    path('post_new', new_post, name='new_post'),
    path('post_edit/<post_id>', edit_post, name='edit_post'),
    path('post_delete/<post_id>', delete_post, name='delete_post')
    ]