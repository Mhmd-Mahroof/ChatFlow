# Generated by Django 4.2.7 on 2023-12-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.ImageField(null=True, upload_to='room_images'),
        ),
    ]