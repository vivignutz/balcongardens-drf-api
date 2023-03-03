from django.db import models
from django.contrib.auth.models import User


class Plants(models.Model):
    """
    Model that provides the fields to create/retrieve/update
    list of plants offered to exchange in the db by the user
    instance. Posts opens only for logged in users.
    Image required, that should be uploaded by the owner.
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
        ('salads', 'Salads'),
        ('strawberries', 'Strawberries'),
        ('suculents', 'Suculents'),
        ('tomatoes', 'Tomatoes'),
        ('water_lily', 'Water Lily'),
        ('other', 'Other')
    ]

    difficulty_level_choices = [
        ('1', 'Low'),
        ('2', 'Moderate'),
        ('3', 'High'),
        ('4', 'Expert'),
        ('5', 'Almost impossible!')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=80)
    specie = models.CharField(
        max_length=32, choices=image_filter_choices
    )
    difficulty_level = models.CharField(
        max_length=32, choices=difficulty_level_choices, default=None
    )
    email = models.CharField
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=15)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rb5ucj', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
