# Generated by Django 3.2 on 2022-04-22 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_rename_text_tweet_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
