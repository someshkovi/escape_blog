# Generated by Django 3.2 on 2022-04-16 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contet',
            new_name='content',
        ),
    ]
