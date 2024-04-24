from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id': 1, "name": "Let's learn Python!"},
#     {'id': 2, "name": "Let's learn Javascript!"},
#     {'id': 3, "name": "Let's learn SQL!"}
# ]

#1 def home(request):
#     # return HttpResponse("<h1>Home Page<h1>")
#     return render(request, "home.html", {'rooms': rooms})

#2 def home(request):
#     context = {'rooms': rooms}
#     return render(request, "base/home.html", context)

def home(request):
    rooms = Room.objects.all() #get, filter, exclude
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)

# def room(request, pk):
#     # return HttpResponse("<h1>Room<h1>")
#     room = None
#     for i in rooms:
#         if i["id"] == int(pk):
#             room = i
#     context = {"room": room}
#     return render(request, "base/room.html", context)

def room(request, pk):
    # return HttpResponse("<h1>Room<h1>")
    room = Room.objects.get(id=int(pk))
    context = {"room": room}
    return render(request, "base/room.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        # print(request.POST)
        # print(request.POST.get('name'))
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})