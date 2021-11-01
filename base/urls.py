from django.urls import path
from .views.home_view import home
from .views.room_view import room, create_room, update_room, delete_room
from .views.auth_view import login_view, logout_view, register_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('room/<str:pk>/', room, name='room'),
    path('create_room/', create_room, name='create_room'),
    path('update_room/<int:id>', update_room, name='update_room'),
    path('delete_room/<int:id>', delete_room, name='delete_room'),
]
