# Generated by Django 4.0.3 on 2022-04-18 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0028_alter_redessociales_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redessociales',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
