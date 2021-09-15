from django.shortcuts import render
from django.http.response import Http404
from .models import Comment, Reply
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer


class CreateComment(APIView):
    def get(self, request):
        comment= Comment.objects.all()
        serializer= CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer= CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class CreateReply(APIView):

    def get_object(self, fk):
        try:
            return Comment.objects.get(fk=fk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)




# Create your views here.
