from django.shortcuts import render,HttpResponse
from accounts.models import CustomUser
from .models import Todo
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    template = "todoapp/index.html"
    args = {}
    users = CustomUser.objects.all()
    tasks = Todo.objects.all()
    print(users)
    args['users']=users
    args['tasks']=tasks
    return render(request,template,args)


def onboarding(request):
    template = "todoapp/onboarding.html"
    args = {}
    return render(request,template,args)


@csrf_exempt
def create_task(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    objects = {}
    response = {}
    for key,val in json_data.items():
        objects[key]=val
    # create a new task
    try:
        task = Todo()
        task.title = objects['title']
        task.description = objects['description']
        task.due_date = objects['due_date']
    except KeyError as e:
        response['success']=False
        response['message']= "Please provide "+str(e)
    except Exception as e:
        response['success']=False
        response['message']=str(e)
    else:
        task.save()
        response['success']=True
        response['message']="Task created"
    dump = json.dumps(response)
    return HttpResponse(dump, content_type='application/json')
