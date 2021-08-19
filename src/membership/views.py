from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required
#from django.shortcuts import HttpResponseRedirect

# Create your views here.


#USER ONLY

def signupuser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try: 
                user = User.objects.create_user(
                    request.POST['username'], 
                    first_name=request.POST['first_name'], 
                    last_name=request.POST['last_name'], 
                    email=request.POST['email'] , 
                    password=request.POST['password1'])
                perfil = Member.objects.create(
                    user = User.objects.all().last(),
                    profile_picture=request.FILES['img'])
                
                user.save()
                perfil.save()
                
                return redirect('home')
            except IntegrityError:
                error = 'Tu nombre de usuario fue tomado, intenta con otro'
                context = {
                    'error':error,
                    'form': form,
                }
                return render(request, 'members/signupuser.html', context)
        else:
            error = 'Error al escribir tu contrasena'
            context={'error':error,
                    'form': form,}
            return render(request, 'members/signupuser.html', context)
    else:
        context={
            'form': form
        }
        return render(request, 'members/signupuser.html', context)


#USER ONLY
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['Password'])
        if user is None:
            return render(request, 'members/loginuser.html', {'form': AuthenticationForm() , 'error': 'User or password did not match'})
        else:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'members/loginuser.html',  {'form': AuthenticationForm()})


