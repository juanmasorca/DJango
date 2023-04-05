from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    titulo = "Welcome to Django APP"
    return render(request, 'index.html', {
        'title': titulo
    })


def about(request):
    return render(request, 'about.html')


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


# def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
def projects(request):
    projects = Project.objects.all()
    return render(request, 'project/project.html', {
        'project': projects
    })


# def tasks(request, id):
    # Result = Task.objects.get(id=id)
    # Result = get_object_or_404(Task, id=id)
    # return HttpResponse('task: %s' % Result.title)
def tasks(request):
    Result = Task.objects.all()
    return render(request, 'task/task.html', {
        'task': Result
    })


def create_task(request):
    if request.method == 'GET':
        # sow interface
        return render(request, 'task/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('/tasks/')


def create_project(request):
    if request.method == 'GET':
        # sow interface
        return render(request, 'project/create_project.html', {
            'form': CreateNewProject()})
    else:
        Project.objects.create(
            name=request.POST['name'])
        return redirect('projects')


def project_detail(request, id):
    # project_id=Project.objects.GET(id=id)
    project_id = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'project/detail.html', {
        'project_id': project_id,
        'tasks': tasks
    })
