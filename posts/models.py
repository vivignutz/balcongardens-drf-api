from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    Filter for image choice.
    """

    image_filter_choices = [
        ('amaryllis', 'Amaryllis'),
        ('begonia', 'Begonia'),
        ('bulbs', 'Bulbs'),
        ('cactus', 'Cactus'),
        ('chillis', 'Chillis'),
        ('chinese_money_plant', 'Chinese money plant'),
        ('dragon_tree', 'Dragon Tree'),
        ('grape_ivy', 'Grape Ivy'),
        ('herbs', 'Herbs'),
        ('hop', 'Hop'),
        ('kelvin', 'Kelvin'),
        ('monstera_deliciosa', 'Monstera Deliciosa'),
        ('oregano_tree', 'Oregano Tree'),
        ('strawberries', 'Strawberries'),
        ('suculents', 'Suculents'),
        ('tomatoes', 'Tomatoes'),
        ('water_lily', 'Water Lily')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
            upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
        )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

