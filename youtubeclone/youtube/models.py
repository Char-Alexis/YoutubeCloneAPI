from django.db import models

# Create your models here.
class Youtube(models.Model):
    comment = models.CharField(max_length=500)
