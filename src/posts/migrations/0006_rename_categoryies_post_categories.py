# Generated by Django 4.0.4 on 2022-04-16 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_category_post_categoryies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoryies',
            new_name='categories',
        ),
    ]
