# Generated by Django 4.0.3 on 2022-03-27 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_rename_nombre_productos_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='nombre',
            new_name='titulo',
        ),
    ]