from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.CreateComment.as_view()),
    path('youtube/<int:fk>/', views.CreateReply.as_view()),
]