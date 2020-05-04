from django.contrib import admin
from .models import Message
from .models import Option, Riddle
from .models import Mark

admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Message)
admin.site.register(Mark)