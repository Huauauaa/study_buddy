from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from base.forms.MessageForm import MessageForm
from base.models.Message import Message


@login_required(login_url='login')
def delete_message(request, id):
    message = Message.objects.get(id=id)
    room_id = message.room.id
    if request.method == 'POST':
        if request.user != message.user:
            return HttpResponse('You are not allowed here!!!')
        message.delete()
        return redirect('room', room_id)
    return render(request, 'delete_confirm.html', {'item': message})


@login_required(login_url='login')
def update_message(request, id):
    instance = Message.objects.get(id=id)
    form = MessageForm(instance=instance)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(request.META.HTTP_REFERER)
    return render(request, 'base/form.html', {'form': form})
