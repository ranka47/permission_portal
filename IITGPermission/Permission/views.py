from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from Permission import forms
from Permission.models import Task, Template
from django.contrib.auth.models import Group


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
    return HttpResponseRedirect('/Permission/')


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

def user_has_tasks(username, tasks):
    for task in tasks:
        if task.user_name == username:
            return True
    return False

@login_required(login_url="/Permission/")
def home(request):
    """
    displays home page for user, with his previous tasks
    """
    task_list=Task.objects.all()
    # if no previous tasks return message instead of table
    full_name = request.user.username
    return render_to_response('Permission/home.html',
                            {'full_name': full_name.capitalize(),
                            'username':request.user.username,
                            'tasks':task_list,
                            'user_has_tasks':user_has_tasks(request.user.username, task_list)},
                            context_instance=RequestContext(request))


def user_detail(request, task_id):

    task = Task.objects.get(id=task_id)
    return render(request, 'Permission/user_detail.html', {'task':task})

@login_required(login_url="/Permission/")
def new_permission(request):
    """
    displays new permission form for the user and processes it
    """
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            
            task = form.save(commit=False)
            task.current_group=task.template_id.templategroup_set.get(number=1).group
            task.user_name = request.user.username
            task.save()
            
            form.fields['user_department'].widget.attrs['readonly']=True
            form.fields['user_designation'].widget.attrs['readonly']=True
            form.fields['from_date'].widget.attrs['readonly']=True
            form.fields['to_date'].widget.attrs['readonly']=True
            form.fields['purpose'].widget.attrs['readonly']=True
            form.fields['facilities_required'].widget.attrs['readonly']=True
            return render_to_response("Permission/submitted.html", {'form':form, 'task':task,}, context_instance=RequestContext(request))
    else: 
        form = forms.TaskForm()

    return render_to_response("Permission/new_permission.html", {'form':form}, context_instance=RequestContext(request))


def group_has_tasks(groups, tasks):
    for task in tasks:
        for group in groups:
            if task.current_group == group:
                return True
    return False

@login_required(login_url="/Permission/")
@staff_member_required
def pending_permissions(request):
    """
    displays home page for user
    """
    task_list=Task.objects.all()
    groups=request.user.groups.all()
    return render_to_response('Permission/pending.html',
                            {'full_name': request.user,
                            'groups':groups,
                            'tasks':task_list,
                            'group_has_tasks': group_has_tasks(groups, task_list),},
                            context_instance=RequestContext(request))

    

@login_required(login_url="/Permission/")
@staff_member_required
def done_permission(request):
    task_list=Task.objects.all()
    groups=request.user.groups.all()
    return render_to_response('Permission/permission_done.html',
                            {'full_name': request.user,
                            'groups':groups,
                            'tasks':task_list,},
                            context_instance=RequestContext(request))
    
@login_required(login_url="/Permission/")
@staff_member_required
def new_template(request):
    return HttpResponse('template_new')
    pass
    
@login_required(login_url="/Permission/")
@staff_member_required
def existing_template(request):
    return HttpResponse('template_existing')

@login_required(login_url="/Permission/")
@staff_member_required
def detail(request, task_id):

    task = Task.objects.get(id=task_id)
    return render(request, 'Permission/detail.html', {'task':task})

def admin_is_in_current_group(task, groups):
    for group in groups.all():
        if task.current_group==group:
            return True
        else:
            return False
@login_required(login_url="/Permission/")
@staff_member_required
def accepted(request, task_id):
    task = Task.objects.get(id=task_id)
    groups = request.user.groups.all()
    if admin_is_in_current_group(task, groups):
        task.comment=task.comment+"Approved by: "+request.user.username+"\n"
        task.level=task.level+1
        task.done_level=task.done_level+1
        count=0
        for num in task.template_id.templategroup_set.all():
            if num.number != 0:
                 count=count+1
        if task.level==count+1:
            task.status="Accepted"
            task.current_group=None
        else:
            task.status="Pending"
            task.current_group=task.template_id.templategroup_set.get(number=task.level).group
        task.save()
        task_list=Task.objects.all()
        groups=request.user.groups.all()
        return HttpResponseRedirect('/Permission/pending-permissions/')
    else:
        return HttpResponseRedirect('/Permission/pending-permissions/')

@login_required(login_url="/Permission/")
@staff_member_required
def denied(request, task_id):
    task = Task.objects.get(id=task_id)
    groups = request.user.groups.all()
    if admin_is_in_current_group(task, groups):
        task.level=-1
        task.current_group=None
        task.status="Denied"
        task.save()
        task_list=Task.objects.all()
        groups=request.user.groups.all()
        return HttpResponseRedirect('/Permission/pending-permissions/')    
    else:
        return HttpResponseRedirect('/Permission/pending-permissions/')    
