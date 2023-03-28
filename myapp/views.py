from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("HelloWord")


def about(request):
    return HttpResponse("About")
