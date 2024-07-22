from django import forms
from .models import Vendor, Tender

class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact', 'email', 'address', 'gst_number']

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact.isdigit():
            raise forms.ValidationError('Contact number should contain only digits.')
        if len(contact) != 10:
            raise forms.ValidationError('Contact number should be 10 digits long.')
        return contact


    def clean_gst_number(self):
        gst_number = self.cleaned_data.get('gst_number')
        if len(gst_number) != 15:
            raise forms.ValidationError('GST number should be 15 characters long.')
        return gst_number

class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['title', 'description', 'image', 'document']

class ContactNumberForm(forms.Form):
    contact_number = forms.CharField(max_length=15)