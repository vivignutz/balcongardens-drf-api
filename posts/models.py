from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
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
    title = models.CharField(
        max_length=80, null=False, blank=False, default='')
    content = models.TextField(
        blank=True, null=False, default='')
    plant_type = models.CharField(
        max_length=32, choices=image_filter_choices,
        null=False, default='')
    difficulty_level = models.CharField(
        max_length=1, choices=difficulty_level_choices,
        null=True, blank=True, default='')
    email = models.CharField
    city = models.CharField(
        max_length=30, null=False, blank=False, default='')
    postal_code = models.CharField(
        max_length=15, null=False, blank=False)
    image = models.ImageField(
            upload_to='images/', default='', blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
