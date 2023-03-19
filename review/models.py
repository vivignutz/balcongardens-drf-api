from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# class Rating(models.Model):
#    stars = models.IntegerField(default=0)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'object_id',)
