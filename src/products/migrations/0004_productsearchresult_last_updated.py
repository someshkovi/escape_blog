# Generated by Django 3.2 on 2022-06-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productsearchresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsearchresult',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
