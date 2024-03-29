from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model that provides the fields to create/retrieve/update
    list of plants offered to exchange in the db by the user
    instance. Posts opens only for logged in users.
    Image required, that should be uploaded by the owner.
    """
    plant_type_choices = [
        ('unknown', 'Unknown'),
        ('amaryllis', 'Amaryllis'),
        ('begonia', 'Begonia'),
        ('bulbs', 'Bulbs'),
        ('chillis', 'Chillis'),
        ('chinese_money_plant', 'Chinese money plant'),
        ('dragon_tree', 'Dragon Tree'),
        ('grape_ivy', 'Grape Ivy'),
        ('herbs', 'Herbs'),
        ('hop', 'Hop'),
        ('monstera_deliciosa', 'Monstera Deliciosa'),
        ('ornamental', 'Ornamental'),
        ('salads', 'Salads'),
        ('berries', 'Berries'),
        ('suculents', 'Suculents'),
        ('tomatoes', 'Tomatoes'),
        ('water_lily', 'Water Lily'),
        ('other', 'Other')
    ]

    difficulty_level_choices = [
        ('1', '1: Low'),
        ('2', '2: Moderate'),
        ('3', '3: High'),
        ('4', '4: Expert'),
        ('5', '5: Almost impossible!')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=80, null=False, blank=False, default='')
    description = models.TextField(
        blank=True, null=False, default='')
    difficulty_level = models.CharField(
        max_length=1, choices=difficulty_level_choices,
        null=True, blank=True, default='')
    plant_type = models.CharField(
        max_length=30, choices=plant_type_choices,
        null=True, blank=True, default='')
    city = models.CharField(
        max_length=30, null=True, blank=False, default='')
    image = models.ImageField(
            upload_to='images/', default='', blank=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
