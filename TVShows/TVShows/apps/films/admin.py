from django.contrib import admin

from .models import Actor, Mark, Film, Comment, Genre

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Comment)
admin.site.register(Mark)
