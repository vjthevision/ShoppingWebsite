from .models import Laptop
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = {
            'title',
            'desc',
            'price',
            'image',
            'featured',
            'category_name',
        }