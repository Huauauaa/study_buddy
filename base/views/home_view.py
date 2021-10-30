from django.shortcuts import render

from base.models.Room import Room


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})