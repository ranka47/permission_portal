from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from Permission import forms


#------------------------------------------------------------
#       User Authentication
#------------------------------------------------------------

def login(request):
    """
    displays login page at the start
    """
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        return render_to_response('Permission/login.html', {'form_errors': form_errors})
    else:
        return render_to_response('Permission/login.html', c)


@login_required(login_url="/Permission")
def logout(request):
    """
    logs out user, only if he is already logged in.
    """
    auth.logout(request)
    return render_to_response('Permission/login.html')


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
        return HttpResponseRedirect('/Permission/home')

    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/Permission/')


# def submitted(request):
    """
    Confirmation after adding Task
    """


#------------------------------------------------------------
#       User's dashboard
#------------------------------------------------------------

@login_required(login_url="/Permission/")
def home(request):
    """
    displays home page for user
    """
    return render_to_response('Permission/home.html',
                            {'full_name': request.user.username})


@login_required(login_url="/Permission/")
def new_permission(request):
    """
    displays new permission form for the user and processes it
    """
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form.fields['user_name'].widget.attrs['readonly']=True
            form.fields['user_department'].widget.attrs['readonly']=True
            form.fields['user_designation'].widget.attrs['readonly']=True
            form.fields['from_date'].widget.attrs['readonly']=True
            form.fields['to_date'].widget.attrs['readonly']=True
            form.fields['purpose'].widget.attrs['readonly']=True
            form.fields['facilities_required'].widget.attrs['readonly']=True
            return render_to_response("Permission/submitted.html", {'form':form},)
    else: 
        form = forms.TaskForm()

    return render_to_response("Permission/new_permission.html", {'form':form}, context_instance=RequestContext(request))
