from django.db import models
from django.contrib.auth.models import User

from behaviors import BaseField
from social.models import ClassRoom

class Student(BaseField) : 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='student', null=True, blank=True)
    name = models.CharField(max_length=64)
    introduce_text = models.TextField()
    class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, related_name='students', null=True, blank=True)
