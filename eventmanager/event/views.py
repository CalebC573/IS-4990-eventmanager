from django.shortcuts import render, redirect
from .models import *


# Create your views here.

# Home page in dev
#def home(request):
#    if request.method == 'GET':
#        return redirect('index.html')
#    return render(request, 'home.html')

# create function for events stored in event\urls.py
def index(request):
    events = Event.objects.all
    if request.method == 'POST':
        new_event = Event(
            
            title = request.POST['title'],
            date = request.POST['date'],
            description = request.POST['description'],
            location = request.POST['location'],
        )
        new_event.save()
        return redirect('/')
    
    return render(request, 'index.html', {'events': events})

#edit function for updating events in event\urls/py
def edit(request, pk):
    events = Event.objects.get(id=pk)
    if request.method == 'POST':
        update_event = Event(
            title = request.POST['new_title'],
            date = request.POST['new_date'],
            description = request.POST['new_description'],
            location = request.POST['new_location']
        )
        events.delete()
        update_event.save()
        return redirect('/')
    return render(request, 'edit.html', {'events': events})

# delete function for deleting events stored in event\urls.py
def delete(request, pk):
    events = Event.objects.get(id=pk)
    events.delete()
    return redirect('/')