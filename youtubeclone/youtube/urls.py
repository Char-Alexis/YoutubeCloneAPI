from django.urls import path
from . import views

urlpatterns = [
    # path('youtube/', views.CommentList.as_view()), #  Get all videos & Post
    path('youtube/<str:video_id>/video', views.CommentList.as_view()), #  Get by video & Post
    path('youtube/<int:pk>', views.CommentDetail.as_view()), # Put & Delete

    path('youtube/reply/<str:comment_id>/video', views.ReplyList.as_view()), # GET & Post
    path('youtube/reply/<int:pk>/', views.ReplyDetail.as_view()), # GET & Post
]