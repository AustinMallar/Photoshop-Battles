from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='post_pictures')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Reply(models.Model):
    title=models.CharField(max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_replying_to=models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reply_pictures')
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def like_list(self):
        liked_list = []
        for u in self.liked_set.all():
            liked_list.append(u.user.username)
        return liked_list

class Liked(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


