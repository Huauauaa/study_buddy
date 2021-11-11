from django.forms import ModelForm
from base.models.User import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'bio']
