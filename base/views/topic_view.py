from django.shortcuts import redirect, render, reverse

from base.models.Topic import Topic
from base.models.Room import Room
from base.models.User import User
from django.db.models import Q


def topics_view(request):
    topics = Topic.objects.all()
    all_rooms = Room.objects.all()
    q = request.GET.get('q') or ''
    topic_name = request.GET.get('topic_name') or ''
    if q or topic_name:
        return redirect('{}?q={}'.format(reverse('home'), q))

    return render(
        request,
        'base/topics.html',
        {
            'topics': topics,
            'all_rooms': all_rooms,
        },
    )
