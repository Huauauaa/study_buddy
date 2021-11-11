from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models.User import User
from base.forms.UserCreateForm import UserCreateForm
from django.contrib.auth.hashers import make_password


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next') or 'home')
            else:
                messages.error(request, 'email or password is wrong.')
        except:
            messages.error(request, 'email or password is wrong.')
    return render(request, 'base/login_register.html', {'page': 'login'})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(request.POST.get('password1'))
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error during registration')

    return render(request, 'base/login_register.html', {'form': form})
