from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.utils import tree
from django.views.generic.base import TemplateResponseMixin
from behaviors import BaseField

class ClassRoom(BaseField) :
    class_num = models.IntegerField()
    teacher = models.CharField(max_length=64)

class Comment(BaseField) :
    content = models.TextField(max_length=64)
    writer = models.ForeignKey(User, on_delete=SET_NULL, related_name='writer',null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=SET_NULL, related_name='owner',null=True, blank=True)

class Like(BaseField) :
    comment = models.OneToOneField(Comment, on_delete=SET_NULL, related_name='like', null=True, blank=True)
    users = models.ManyToManyField(User, related_name='like', blank=True)

class Relationship(BaseField) :
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relationship', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)