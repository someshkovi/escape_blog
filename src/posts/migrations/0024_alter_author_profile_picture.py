# Generated by Django 3.2 on 2022-04-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_rename_published_date_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
