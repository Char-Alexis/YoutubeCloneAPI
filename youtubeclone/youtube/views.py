from django.http.response import Http404
from .models import Comment
from .models import Reply
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .serializers import ReplySerializer


class CommentAllList(APIView):
    def get(self, request):
        comment= Comment.objects.all()
        serializer= CommentSerializer(comment, many=True)
        return Response(serializer.data)

class CommentList(APIView):
    def get_byVideo(self, request, video):
        comments = Comment.objects.filter(video_id =video)
        serializer= CommentSerializer(comments, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer= CommentSerializer(data=request.data)
        # serializer.video_id=video_id
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        
    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReplyList(APIView):
    def get(self, request, comment):
        reply = Reply.objects.filter(orig_comment_id=comment)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer= ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class ReplyDetail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, video_id):
        reply = self.get_object(video_id)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)


