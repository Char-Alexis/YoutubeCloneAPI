from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    video_id= models.CharField(max_length=500)
    like= models.IntegerField()
    dislike= models.IntegerField()

    def __init__(self):
        return self.name

class Reply(models.Model):
    reply_text = models.CharField(max_length=500)
    comment_id = models.ForeignKey(Comment , on_delete=models.CASCADE)

    def __init__(self):
        return self.name
