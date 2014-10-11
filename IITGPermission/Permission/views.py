from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth

from Permission.models import TaskForm


#------------------------------------------------------------
#       User Authentication Views
#------------------------------------------------------------

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('Permission/login.html', c)

def loggedin(request):
    return render_to_response('Permission/loggedin.html',
                            {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('Permission/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('Permission/logout.html')


def auth_view(request):
    """
    Authenticates user from the username and password from POST
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        # Since the user is authenticated, Log the user in.
        auth.login(request, user)
        return HttpResponseRedirect('Permission/loggedin')

    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('Permission/invalid')


#------------------------------------------------------------
#       User's New Permission Form
#------------------------------------------------------------

def new_permission(request):
        form = TaskForm()
        return render_to_response('Permission/new_permission.html', {'form': form})

def new_permission_submitted(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else: 
            form = TaskForm()
            return render_to_response('Permission/new_permission.html', {'form': form})
    else: 
        form = TaskForm()
        return HttpResponseRedirect('Permission/new/', {'form': form})
