from django.shortcuts import render


rooms = [
    {'id': 1001, 'name': 'JavaScript'},
    {'id': 1002, 'name': 'Java'},
    {'id': 1003, 'name': 'Python'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = next((x for x in rooms if x['id'] == int(pk)), None)
    return render(request, 'base/room.html', {'room': room})
