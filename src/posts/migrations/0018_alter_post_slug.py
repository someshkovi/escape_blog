# Generated by Django 3.2 on 2022-04-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
