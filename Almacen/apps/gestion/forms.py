from django import forms

from .models import Category

class ProductForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255, min_length=1, required=True)
    description= forms.CharField(label="Description", required=True, widget=forms.Textarea(attrs={ 'rows':1, 'cols':20 }))
    price = forms.FloatField(min_value=0.1)
    category = forms.ModelChoiceField(label="Category", queryset=Category.objects.all())