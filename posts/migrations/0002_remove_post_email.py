# Generated by Django 3.2.18 on 2023-03-20 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
    ]