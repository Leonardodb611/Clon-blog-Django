# Generated by Django 4.0.3 on 2022-03-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_blog_id_alter_blogs_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('precio', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]
