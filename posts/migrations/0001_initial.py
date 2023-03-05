# Generated by Django 3.2.18 on 2023-03-05 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=80)),
                ('content', models.TextField(blank=True, default='')),
                ('image_filter', models.CharField(choices=[('amaryllis', 'Amaryllis'), ('begonia', 'Begonia'), ('bulbs', 'Bulbs'), ('cactus', 'Cactus'), ('chillis', 'Chillis'), ('chinese_money_plant', 'Chinese money plant'), ('dragon_tree', 'Dragon Tree'), ('grape_ivy', 'Grape Ivy'), ('herbs', 'Herbs'), ('hop', 'Hop'), ('kelvin', 'Kelvin'), ('monstera_deliciosa', 'Monstera Deliciosa'), ('oregano_tree', 'Oregano Tree'), ('salads', 'Salads'), ('strawberries', 'Strawberries'), ('suculents', 'Suculents'), ('tomatoes', 'Tomatoes'), ('water_lily', 'Water Lily'), ('other', 'Other')], default='', max_length=32)),
                ('image', models.ImageField(blank=True, default='../default_post_rgq6aq', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
