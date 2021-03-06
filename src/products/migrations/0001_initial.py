# Generated by Django 3.2 on 2022-05-26 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(choices=[('amazon.in', 'amazon india'), ('flipkart.com', 'flipkart'), ('amazon.com', 'amazon us')], default='amazon.in', max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
                ('sub_category', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('category', 'sub_category')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('max_price', models.IntegerField(blank=True, null=True)),
                ('min_price', models.IntegerField(blank=True, null=True)),
                ('target_price', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('₹', 'Rupee(INR)'), ('$', 'Dollar(US)'), ('other', 'other')], default='₹', max_length=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('availabity_messsage', models.CharField(blank=True, max_length=100, null=True)),
                ('availabity', models.BooleanField(blank=True, default=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcategory')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.websites')),
            ],
            options={
                'ordering': ['category', 'name'],
            },
        ),
    ]
