from django.shortcuts import render, redirect
from .forms import EntryForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
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

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()           

            return redirect('/accounts/login/')


    context = {'form':form}

    return render(request, 'register.html', context=context)