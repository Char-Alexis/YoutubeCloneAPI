from rest_framework import serializers
from .models import Comment
from .models import Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment_text', 'video_id', 'like', 'dislike']

        def create(self, validated_data):
            return Comment.objects.create(**validated_data)


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'reply_text', 'orig_comment_id']

        # def create(self, validated_data):
        #     return Reply.objects.create(**validated_data)