from django.db import models
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    ts = models.DateTimeField('Date Created')
    slug = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        return super(Post, self).save()


