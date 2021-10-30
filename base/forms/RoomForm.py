from django import forms

from base.models.Room import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
