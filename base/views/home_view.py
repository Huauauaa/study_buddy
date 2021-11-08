from django.shortcuts import render
from django.db.models import Q

from base.models.Room import Room
from base.models.Topic import Topic
from base.models.Message import Message


def home(request):
    q = request.GET.get('q') or ''
    topic_name = request.GET.get('topic_name') or ''
    all_rooms = Room.objects.all()
    if topic_name:
        rooms = all_rooms.filter(topic__name=topic_name)
    else:
        rooms = all_rooms.filter(
            Q(topic__name__icontains=q) | Q(name__icontains=q)
        )
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(room__in=rooms).order_by('-created')

    return render(
        request,
        'base/home.html',
        {
            'rooms': rooms,
            'topics': topics,
            'room_count': rooms.count(),
            'q': q,
            'room_messages': room_messages,
            'topic_name': topic_name,
            'all_rooms': all_rooms,
        },
    )
