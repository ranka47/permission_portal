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
from Permission import models
from django.contrib.auth.models import Group, User
from Permission import pdf
import datetime, os

# Extensions allowed for uploading documents for the request asked
extensions = ['.jpg','.jpeg','.pdf','.png','']

def findReviewedTasks(user):
    checkStr = user.username + "->"
    reviewedTasks = []
    tasks = models.Task.objects.all()
    for task in tasks:
        lastUser = "->" + user.username
        if checkStr in task.status_description or lastUser in task.status_description:
            reviewedTasks.append(task)
    return reviewedTasks
    
def findLastUser(task):
    lastUser = ""
    i = -1
    char = task.status_description[i]
    while(char!='>'):
        lastUser = char + lastUser 
        i=i - 1
        char = task.status_description[i]
    return lastUser
    
def findFirstUser(task):
    firstUser = ""
    i=0
    char = task.status_description[i]
    while(char!='-'):
        firstUser = firstUser + char
        i = i + 1
        char = task.status_description[i]
    return firstUser
#------------------------------------------------------------
#       User Authentication
#------------------------------------------------------------

def login(request):
    """
    displays login page at the start
    """
    c = {}
    c.update(csrf(request))
    return render_to_response('Permission/login.html', c)


@login_required(login_url="/Permission")
def logout(request):
    """
    logs out user, only if he is already logged in.
    """
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
        return HttpResponseRedirect('/Permission/home')

    else:
        # Return an 'invalid login' error message.
        return render(request,'Permission/login.html',{
            'form_errors':True,
            })

#------------------------------------------------------------
#       User's dashboard
#------------------------------------------------------------



@login_required(login_url="/Permission/")
def home(request):
    """
    displays home page for user, with his previous tasks
    """
    # tasks=models.Task.objects.all()
    full_name = request.user.first_name+" "+request.user.last_name
    myTasks = []
    for task in models.Task.objects.all():
        if findFirstUser(task) == request.user.username:
            myTasks.append(task)
    return render_to_response('Permission/home.html',{
        'tasks':myTasks,
        'full_name':full_name,

        })

@login_required(login_url="/Permission/")
def new_permission(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST, request.FILES)
        users = User.objects.all()
        users = users.exclude(username=request.user.username)
        fileExtension = ''
        # return HttpResponse(request.path)
        try:
            fileExtension = os.path.splitext(request.FILES['required_files'].name)[1]
        except:
            pass
        if form.is_valid() and fileExtension in extensions:
            task = form.save(commit=False)
            task.applicant = request.user.username+" ("+request.user.first_name+" "+request.user.last_name+")"
            task.date_of_application = datetime.datetime.now()
            task.status = "Pending"
            task.status_description = request.user.username+"->"+request.POST['user']
            task.save()
            return HttpResponseRedirect('/Permission/home')
        elif form.is_valid() and fileExtension not in extensions:
            return render(request, 'Permission/new_permission.html',{'form':form,
                        'success':False,
                        'users':users,
                        'message':"You can upload .jpg, .jpeg, .pdf and .png files only"})
        else:
            return render(request, 'Permission/new_permission.html',{
                'form':form,
                'success':False,
                'users':users,
                'message':"Please correct the errors and submit again."
                })
    else:
        form=forms.TaskForm()
        users=User.objects.all()
        users = users.exclude(username=request.user.username)

        return render(request, 'Permission/new_permission.html',{
            'users':users,        
            'form':form,
            })

@login_required(login_url="/Permission")
def pending(request):
    revUser = request.user.username[::-1]+">"
    tasks = models.Task.objects.all()
    pendingTasks=[]
    for task in tasks:
        revDesc = task.status_description[::-1]
        if revDesc.startswith(revUser) and task.status == "Pending":
            pendingTasks.append(task)
    return render(request, 'Permission/pending.html',{
        'pendingTasks':pendingTasks,
        })

@login_required(login_url="/Permission")
def reviewed(request):
    return render(request, 'Permission/reviewed.html',{
        'reviewedTasks':findReviewedTasks(request.user),
        })

@login_required(login_url="/Permission")
def getPDF(request, task_id):
    return pdf.pdf_gen(models.Task.objects.get(id=task_id))


@login_required(login_url="/Permission")
def details(request, task_id):
    task = models.Task.objects.get(id=task_id)
    users = User.objects.all().exclude(username=request.user.username)
    commentForm = forms.CommentForm()
    showOptions = False
    if task.status == "Pending":
        showOptions = True
    if request.method == "POST":
        task.status_description = task.status_description + "->" + request.POST['user']
        task.save()
        return render(request, 'Permission/reviewed.html',{
            'reviewedTasks':findReviewedTasks(request.user),
            })
    return render(request, 'Permission/details.html',{
        'task':task,
        'user':request.user,
        'lastUser':findLastUser(task),
        'firstUser':findFirstUser(task),
        'showOptions':showOptions,
        'users':users,
        'commentForm':commentForm,
        })

@login_required(login_url="/Permission")
def accepted(request, task_id):
    task = models.Task.objects.get(id=task_id)
    task.status = "Accepted"
    task.save()
    return render(request, 'Permission/reviewed.html',{
            'reviewedTasks':findReviewedTasks(request.user),
        })

@login_required(login_url="/Permission")
def denied(request, task_id):
    task = models.Task.objects.get(id=task_id)
    task.status = "Denied"
    task.save()
    return render(request, 'Permission/reviewed.html',{
            'reviewedTasks':findReviewedTasks(request.user),
        })

@login_required(login_url="/Permission")
def delete(request, task_id):
    models.Task.objects.get(id=task_id).delete()
    full_name = request.user.first_name+" "+request.user.last_name
    myTasks = []
    for task in models.Task.objects.all():
        if findFirstUser(task) == request.user.username:
            myTasks.append(task)
    return HttpResponseRedirect('/Permission/home')

@login_required(login_url="/Permission")
def edit(request, task_id):
    users = User.objects.all()
    users = users.exclude(username=request.user.username)
    if request.method == "POST":
        fileExtension = ''
        try:
            fileExtension = os.path.splitext(request.FILES['required_files'].name)[1]
        except:
            pass
        form = forms.TaskForm(request.POST, request.FILES)
        if form.is_valid() and fileExtension in extensions:
            task = form.save(commit=False)
            editTask = models.Task.objects.get(id=task_id)
            editTask.permission_type = request.POST['permission_type']
            editTask.subject = request.POST['subject']
            editTask.description = request.POST['description']
            editTask.special_mentions = request.POST['special_mentions']
            
            ############# Hard Coded ###############
            if not editTask.required_files:
                editTask.required_files = request.FILES['required_files']
            ########################################
            
            editTask.urgency = datetime.datetime(int(request.POST['urgency_year']), int(request.POST['urgency_month']), int(request.POST['urgency_day']))
            editTask.status_description = editTask.status_description + "->TaskEdited on " + str(datetime.datetime.now().date()) + " ->" + request.POST['user']
            editTask.save()
            return HttpResponseRedirect('/Permission/home')
        elif fileExtension not in extensions:
            return render(request, 'Permission/new_permission.html',{
                'users':users,
                'form':form,
                'edit':True,
                'task_id':task_id,
                'success':False,
                'message':"You can upload .jpg, .jpeg, .pdf and .png files only",
                })
        else:
            return render(request, 'Permission/new_permission.html',{
                'users':users,
                'form':form,        
                'edit':True,
                'task_id':task_id,
                'success':False,
                'message':"Correct the error and resubmit the form."
                })
    form = forms.TaskForm(None, instance = models.Task.objects.get(id=task_id))

    return render(request, 'Permission/new_permission.html',{
        'form':form,
        'users':users,
        'edit':True,
        'task_id':task_id,
        })
    
@login_required(login_url='/Permission')
def comment(request, task_id):
    task = models.Task.objects.get(id=task_id)
    users = User.objects.all().exclude(username=request.user.username)
    commentForm = forms.CommentForm()
    showOptions = False
    if task.status == "Pending":
        showOptions = True
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.task = task
            temp.user = request.user.username
            form.save()
    
    return HttpResponseRedirect('/Permission/'+task_id+'/user')