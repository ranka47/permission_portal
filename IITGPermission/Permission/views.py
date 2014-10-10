from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.contrib import auth


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



