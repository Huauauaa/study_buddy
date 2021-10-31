from django.shortcuts import render
from django.db.models import Q

from base.models.Room import Room
from base.models.Topic import Topic


def home(request):
    q = request.GET.get('q') or ''
    topic_name = request.GET.get('topic_name') or ''
    if topic_name:
        rooms = Room.objects.filter(topic__name=topic_name)
    else:
        rooms = Room.objects.filter(
            Q(topic__name__icontains=q) | Q(name__icontains=q)
        )
    topics = Topic.objects.all()

    return render(
        request,
        'base/home.html',
        {'rooms': rooms, 'topics': topics, 'room_count': rooms.count(), 'q': q},
    )
