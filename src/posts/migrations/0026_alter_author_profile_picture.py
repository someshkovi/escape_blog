# Generated by Django 3.2 on 2022-04-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_alter_author_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]