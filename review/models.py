from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Rating(models.Model):
    stars = models.IntegerField()