# Generated by Django 4.0.3 on 2022-04-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applogin', '0014_alter_redessociales_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redessociales',
            name='facebook',
            field=models.URLField(blank=True, default='no existen redes', max_length=500),
        ),
        migrations.AlterField(
            model_name='redessociales',
            name='instagram',
            field=models.URLField(blank=True, default='no existen redes', max_length=500),
        ),
        migrations.AlterField(
            model_name='redessociales',
            name='twitter',
            field=models.URLField(blank=True, default='no existen redes', max_length=500),
        ),
    ]