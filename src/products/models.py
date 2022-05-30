from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User

class ProductCategory(models.Model):
    category = models.CharField(max_length=50, unique=True)
    sub_category = models.CharField(max_length=50)

    class Meta:
        unique_together =('category', 'sub_category',)

    def __str__(self) -> str:
        return f'{self.category} > {self.sub_category}'

class Websites(models.Model):
    amazon_in = 'amazon.in'
    flipkart = 'flipkart.com'
    amazon_us = 'amazon.com'
    website_choices = [
        (amazon_in, 'amazon india'),
        (flipkart, 'flipkart'),
        (amazon_us, 'amazon us')
    ]
    site = models.CharField(max_length=24, choices=website_choices, default=amazon_in)
    def __str__(self) -> str:
        return self.site

class Product(models.Model):
    url = models.CharField(max_length=250, null=True, blank=True)
    site = models.ForeignKey(Websites, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)
    min_price = models.IntegerField(null=True, blank=True)
    target_price = models.IntegerField(null=True, blank=True)
    INR = '₹'
    USD = '$'
    currency_choices = [
        (INR, 'Rupee(INR)'),
        (USD, 'Dollar(US)'),
        ('other', 'other'),
    ]
    currency = models.CharField(max_length=6, choices=currency_choices, default=INR)
    rating = models.DecimalField(decimal_places=2, max_digits=4,null=True, blank=True)
    availabity_messsage = models.CharField(max_length=100, null=True, blank=True)
    availabity = models.BooleanField(default=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    class Meta:
        ordering = ['category','name']
        # constraints = [
        #     UniqueConstraint(fields=[name, 'url'], name='name_url_unique')
        # ]
    def __str__(self) -> str:
        return f'{self.name}'