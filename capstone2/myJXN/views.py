from django.shortcuts import render, redirect
from .models import Entry
from rest_framework import generics
from .forms import EntryForm, CreateUserForm
from django.urls import reverse
from .serializers import EntrySerializer
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm

class ListEntry(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class DetailEntry(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

def town(request):
    return render(request, 'index.html')

    
def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myJXN.html', context)

def report(request):
    models = []
    for entries in Entry.objects.all():
        models.append(entries)
    
    print(models)    
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = EntryForm()
            return HttpResponseRedirect(reverse('myJXN:report'))
    else:
        form = EntryForm()
    context = {
        'form':form,
    }
    
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