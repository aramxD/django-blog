from django.core import paginator
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render, get_object_or_404, reverse
from .models import *
from marketing.models import Signup # Este es para capturar emails

from .utils import *
from membership.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# For IP ADREES
def get_ip(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip= x_forward
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ""
    return ip
    
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
    # next_prev_post = posts_list.get(id=post_id)
    next_id = int(post_id)+1
    next_obj = posts_list.filter(id__gt=post.id).order_by('id').first()
    previous_id = int(post_id)-1
    previous_obj = posts_list.filter(id__lt=post.id).order_by('id').last()
    

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


    #Count View 
     
    #PostView.objects.get_or_create(user=request.user, post=post, ip=get_ip(request))
    context={
        'post':post,
         
        'next_obj':next_obj,
        'previous_obj':previous_obj,
        'most_recent_post':most_recent_post,
        'category_count':category_count,
        'form':form,
    }
    return render(request, 'post.html', context)



def new_post(request):
    if request.method == 'POST':
        user = request.user.author
        new_post = PostForm(request.POST, request.FILES)
        if new_post.is_valid():
            post = new_post.save(commit=False)
            post.author = user
            post.save()
            return redirect('home')
    else:
        return render (request, 'post/post_edit.html', {'form':PostForm()})


@login_required
@staff_member_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance= post)
    if request.method == 'POST':
        try:
            form = PostForm(request.POST, request.FILES, instance=post)
            form.save()
            return redirect("post", post_id)
        except ValueError:
            context={
                'form':form,
                'error' : 'Reviza la informacion, algo esta mal...',
                }
            return render(request, 'post/post_edit.html', context)    

    context={
        'form':form,
        }
    return render(request, 'post/post_edit.html', context)


@login_required
@staff_member_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect ('home')


