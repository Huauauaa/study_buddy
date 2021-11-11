from django.shortcuts import render

from base.models.Topic import Topic
from base.models.Room import Room
from base.models.User import User
from django.db.models import Q


def user_profile(request, id):
    user = User.objects.get(id=id)
    topics = Topic.objects.all()

    rooms = user.room_set
    q = request.GET.get('q') or ''
    topic_name = request.GET.get('topic_name') or ''
    if topic_name:
        rooms = rooms.filter(topic__name=topic_name)
    else:
        rooms = rooms.filter(Q(topic__name__icontains=q) | Q(name__icontains=q))

    room_messages = user.message_set.all()

    return render(
        request,
        'base/user_profile.html',
        {
            'user': user,
            'topics': topics,
            'all_rooms': Room.objects.all(),
            'rooms': rooms,
            'room_messages': room_messages,
            'q': q,
        },
    )
