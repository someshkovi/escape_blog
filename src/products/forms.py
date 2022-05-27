from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['url','site', 'name', 'category', 'price'] # thumbnail tbd
        # widgets = {
        #     'body': forms.TextInput(attrs={'placeholder': 'What\'s happening?'}),
        # }