from django.shortcuts import render
from base.models.User import User


def settings_view(request, id):
    if id:
        user = User.objects.get(id=id)
    else:
        user = request.user
    return render(request, 'base/settings.html', {'user': user})
