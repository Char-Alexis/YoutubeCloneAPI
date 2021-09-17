from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.TextField(max_length=500)
    video_id= models.TextField(blank=True, null=True, max_length=15)
    like= models.IntegerField(blank=True, null=True)
    dislike= models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.comment_text

class Reply(models.Model):
    reply_text = models.CharField(max_length=500)
    orig_comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply_text
