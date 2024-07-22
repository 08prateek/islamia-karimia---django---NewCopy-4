from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'contact': forms.TextInput(attrs={'placeholder': 'Your Contact Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Allow names with spaces and alphabets
        if not all(x.isalpha() or x.isspace() for x in name):
            raise forms.ValidationError("Name should only contain letters and spaces.")
        return name

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact.isdigit():
            raise forms.ValidationError("Contact number should only contain digits.")
        if len(contact) < 10 or len(contact) > 15:
            raise forms.ValidationError("Contact number should be between 10 to 15 digits.")
        return contact

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 5:
            raise forms.ValidationError("Message should be at least 5 characters long.")
        return message