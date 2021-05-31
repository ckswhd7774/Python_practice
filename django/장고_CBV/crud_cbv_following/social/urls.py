from django.urls import path
from .views import ClassListView, ClassDetailView
from student.views.crud import CommentView, LikeView, RelationshipView

app_name = 'social'

urlpatterns = [
    path('class-list/', ClassListView.as_view(), name='class_list'),
    path('class/<pk>', ClassDetailView.as_view(), name='class'),
    path('comment/<pk>', CommentView.as_view(), name='comment'),
    path('like/<pk>', LikeView.as_view(), name='like'),
    path('relationship/<pk>', RelationshipView.as_view(), name='relationship'),
]
