from django.contrib.auth.forms import UserCreationForm
from base.models.User import User


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'username', 'password1', 'password2')
