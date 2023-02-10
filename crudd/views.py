from django.shortcuts import render, HttpResponseRedirect
from .forms import *


def add_show(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = Registration()
    else:
     fm = Registration()
    regis = User.objects.all()
    return render(request, 'crudd/add_&_show.html', {'form':fm, 'regis':regis})

def update_data(request, id):
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        fm = Registration(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up = User.objects.get(pk=id)
        fm = Registration(instance=up)
    return render(request, 'crudd/update.html',{'form':fm})


def delete_data(request, id):
    if request.method == 'POST':
        de = User.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')