# Generated by Django 4.0.3 on 2022-04-15 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_alter_avatar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
