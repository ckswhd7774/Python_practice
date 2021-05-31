from django.contrib import admin
from .models import ClassRoom, Comment, Like, Relationship

# Register your models here.
admin.site.register(ClassRoom)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Relationship)