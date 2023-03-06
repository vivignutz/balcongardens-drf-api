from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Rating(models.Model):
    """
    Rating star model, related to User and their Post
    """
    Post = models.ForeignKey(
        Post, related_name='rating', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, null=True, blank=True)
    one = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    two = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    three = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    four = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    five = models.PositiveIntegerField(
        default=0, null=True, blank=True)

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        """
        The string dunder method to evaluate the database
        and return the column with the large number.
        """
        rating_list = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five
        }
        return str(max(rating_list, key=rating_list.get))
