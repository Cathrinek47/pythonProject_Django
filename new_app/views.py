from django.http import HttpResponse


def hello_view(request):
    return HttpResponse("<h1>Hello, friend!</h1>")
