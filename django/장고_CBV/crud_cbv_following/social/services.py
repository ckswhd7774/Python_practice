from django.contrib.auth.models import User
from dataclasses import dataclass

from .models import ClassRoom, Comment, Like, Relationship
class ClassRoomService() :
    @staticmethod
    def find_all() :
        return ClassRoom.objects.all()

class Comment_Service() :
    @staticmethod
    def find_all() :
        return Comment.objects.all()

@dataclass
class LikeDto() :
    comment_pk : str 
    users : User


@dataclass
class RelationshipDto() :
    user_pk : str
    requester : User


class LikeService() :

    @staticmethod
    def find_owner(commnet_pk):
        return Comment.objects.filter(pk=commnet_pk).first().owner

    @staticmethod
    def toggle(dto: LikeDto) :
        comment = Comment.objects.filter(pk=dto.comment_pk).first()
        like = Like.objects.filter(comment__pk=dto.comment_pk).first()

        if like is None :
            like = Like.objects.create(comment = comment)

        if dto.users in like.users.all() :
            like.users.remove(dto.users)

        else :
            like.users.add(dto.users) 

class RelationSevice():
    @staticmethod
    def toggle(dto: RelationshipDto) :
        users = User.objects.filter(pk=dto.user_pk).first()
        relationship = Relationship.objects.filter(users=users).first()
        if relationship is None :
            relationship = Relationship.objects.create(users=users)
        if (dto.requester) in (relationship.followers.all()) :
            relationship.followers.remove(dto.requester)

        else :
            relationship.followers.add(dto.requester)
