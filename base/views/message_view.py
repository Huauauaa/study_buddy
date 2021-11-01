from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from base.models.Message import Message


@login_required(login_url='login')
def delete_message(request, id):
    message = Message.objects.get(id=id)
    room_id = message.room.id
    if request.method == 'POST':
        if request.user.username != message.user:
            return HttpResponse('You are not allowed here!!!')
        message.delete()
        return redirect('room', room_id)
    return render(request, 'delete_confirm.html', {'item': message})
