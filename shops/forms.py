from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'latitude', 'longitude', 'address', 'contact', 'description')
    def clean_name(self):
        name = self.cleaned_data['name']
        if Shop.objects.filter(name=name).exists():
            raise forms.ValidationError("Shop with this name already exists.")
        return name
