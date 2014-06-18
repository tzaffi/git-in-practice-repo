from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def hello_zeph(request):
    return HttpResponse("Hello there Zeph!!!!")
