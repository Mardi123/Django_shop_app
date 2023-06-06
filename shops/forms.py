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
    
    def clean_contact(self):
        contact = self.cleaned_data['contact']
        if not contact.isdigit():
            raise forms.ValidationError("Contact number should contain only digits.")
        if len(contact) != 10:
            raise forms.ValidationError("Contact number should be 10 digits long.")
        return contact
    
    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if latitude < -90 or latitude > 90:
            raise forms.ValidationError("Latitude should be between -90 and 90.")
        return latitude
    
    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if longitude < -180 or longitude > 180:
            raise forms.ValidationError("Longitude should be between -180 and 180.")
        return longitude
