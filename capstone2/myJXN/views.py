from django.shortcuts import render
from .forms import EntryForm
from django.http import HttpResponse

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myJXN.html', context)

def report(request):
    context = {}
        # create object of form
    form = EntryForm(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, 'report.html', context)