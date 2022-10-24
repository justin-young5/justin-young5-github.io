from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myJXN.html', context)