from django.contrib import admin
from base.models.Room import Room
from base.models.Topic import Topic
from base.models.Message import Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
