from django.contrib import admin
from base.models.Room import Room
from base.models.Topic import Topic
from base.models.Message import Message
from base.models.User import User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
