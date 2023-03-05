from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Save(models.Model):
    """
    Model to save a favorite plant, which is being offered
    to swap with others. 'Owner' is a User instance and
    'post' is a Post instance. 'Unique_together' prevent
    a user from saving the same post more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='saved')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
