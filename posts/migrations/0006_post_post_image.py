# Generated by Django 5.1.4 on 2025-03-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='post/1.png', upload_to='post'),
        ),
    ]
