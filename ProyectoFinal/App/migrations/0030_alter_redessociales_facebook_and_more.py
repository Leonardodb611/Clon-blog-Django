# Generated by Django 4.0.3 on 2022-04-18 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_alter_redessociales_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redessociales',
            name='facebook',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='redessociales',
            name='instagram',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='redessociales',
            name='twitter',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]