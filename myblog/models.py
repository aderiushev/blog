from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    ts = models.DateTimeField('Date Created')

    def __str__(self):
        return self.title