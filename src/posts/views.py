from django.db.models import Count, Q

from django.shortcuts import redirect, render, get_object_or_404, reverse
from .models import *
from marketing.models import Signup # Este es para capturar emails
from .utils import *
from membership.models import *
from .forms import *


# Create your views here.
# Funcion para contar categorias


#Funcion para hacer busquedas
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context={
        'queryset':queryset
    }
    return render(request, 'search_results.html', context)



def home(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context={
        'posts_list':featured,
        'post_latest':latest
    }
    return render(request, 'index.html', context)


def blog(request):
    posts_list = Post.objects.all()

    # Codigo del Paginator
    page_request_var = 'page'
    paginated_queryset = info_paginator(posts_list, request, page_request_var)
    
    #Codigo de post recientes
    most_recent_post = recent_post(posts_list)

    # llama la funcion "contador de categorias"
    category_count = get_category_count()
    



    context={
        'posts_list':paginated_queryset,
        'most_recent_post':most_recent_post,
        'page_request_var':page_request_var,
        'category_count':category_count,
    }
    return render(request, 'blog.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #Codigo de post recientes
    posts_list = Post.objects.all()
    most_recent_post = recent_post(posts_list)

    #Next y Previous POSTS
    next_id = int(post_id)+1
    next_obj = posts_list.filter(id=next_id).first()
    previous_id = int(post_id)-1
    previous_obj = posts_list.filter(id=previous_id).first()
    

    #Count Categories
    category_count = get_category_count()

    #Comments
    
    form = CommentForm( request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(request.META['HTTP_REFERER'])
    context={
        'post':post,
        'next_obj':next_obj,
        'previous_obj':previous_obj,
        'most_recent_post':most_recent_post,
        'category_count':category_count,
        'form':form,
    }
    return render(request, 'post.html', context)