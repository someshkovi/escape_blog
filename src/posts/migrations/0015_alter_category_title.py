# Generated by Django 3.2 on 2022-04-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
