from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from base.forms.RoomForm import RoomForm
from base.models.Message import Message
from base.models.Room import Room
from base.models.Topic import Topic


@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    # create message
    if request.method == 'POST':
        Message.objects.create(
            user=request.user, room=room, body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk)

    return render(
        request,
        'base/room.html',
        {
            'room': room,
            'room_messages': room_messages,
            'participants': participants,
        },
    )


@login_required(login_url='login')
def create_room(request):
    topics = Topic.objects.all()
    form = RoomForm()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        (topic, is_new) = Topic.objects.get_or_create(name=topic_name)
        room = Room.objects.create(name=request.POST.get('name'))
        room.host = request.user
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    return render(request, 'base/room-form.html', {'form': form, 'topics': topics})


@login_required(login_url='login')
def update_room(request, id):
    topics = Topic.objects.all()
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        (topic, is_exist) = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    return render(
        request,
        'base/room-form.html',
        {'room': room, 'topics': topics},
    )


@login_required(login_url='login')
def delete_room(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        if request.user != room.host:
            return HttpResponse('You are not allowed here!!!')
        room.delete()
        return redirect('home')
    return render(request, 'delete_confirm.html', {'item': room})
