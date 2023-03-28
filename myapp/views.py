from django.http import HttpResponse, JsonResponse
from .models import Project
# Create your views here.


def index(request):
    return HttpResponse('Index Page')


def hello(request, username):
    print(username)
    return HttpResponse("Hello %s" % username)


def about(request):
    return HttpResponse("About")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request):
    return HttpResponse("Tasks")
