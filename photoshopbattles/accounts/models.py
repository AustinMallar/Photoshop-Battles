from django.db import models
from django.contrib.auth.models import User
from application.models import Reply

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=400, default='Bio..')

    def total_number_likes(self):
        likes = 0
        replies = Reply.objects.filter(user=self.user)
        for r in replies:
            likes+=len(r.like_list())
        return int(likes)


    def __str__(self):
        return f'{self.user.username} Profile'
        
