from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from base.forms.RoomForm import RoomForm
from base.models.Message import Message
from base.models.Room import Room


@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')

    if request.method == 'POST':
        message = Message(
            user=request.user, room=room, body=request.POST.get('body')
        )
        message.save()
        return redirect('room', pk)

    return render(
        request,
        'base/room.html',
        {'room': room, 'room_messages': room_messages},
    )


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', {'form': form})


@login_required(login_url='login')
def update_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', {'form': form})


@login_required(login_url='login')
def delete_room(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        if request.user.username != room.host:
            return HttpResponse('You are not allowed here!!!')
        room.delete()
        return redirect('home')
    return render(request, 'delete_confirm.html', {'item': room})
