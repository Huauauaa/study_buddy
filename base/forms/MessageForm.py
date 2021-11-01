from django import forms

from base.models.Message import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
