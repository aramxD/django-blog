from .models import *
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Conteo de categorias 
def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


# Listado de ultimos 3 posts
def recent_post(posts_list):
    most_recent_post = posts_list.order_by('-timestamp')[0:3]
    return most_recent_post


# Codigo del Paginator
def info_paginator(posts_list, request, page_request_var):
    queryset = posts_list.order_by('id')
    paginator = Paginator(queryset, 4)
    
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage: 
        paginated_queryset = paginator.page(paginator.num_pages) 
    return paginated_queryset

