from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from .models import Comment, Reply

def create_comment(request):
    if request.method == "POST":
        comment_text = request.POST.get('comment_text')
        video_id = request.video_id
        


# Create your views here.
