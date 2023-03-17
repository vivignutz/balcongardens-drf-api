# Generated by Django 3.2.18 on 2023-03-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230315_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
