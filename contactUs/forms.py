from .models import ContactUs
from django import forms




class contactusForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        
        fields = ['firstName','lastName','contact_number','email','company_name','subject','message']
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-input' ,'placeholder': 'نام',}),
            'lastName': forms.TextInput(attrs={'class': 'form-input','placeholder': 'نام خانوادگی',}),
            'contact_number': forms.NumberInput(attrs={'class': 'form-input','placeholder': 'شماره تماس',}),
            'email': forms.EmailInput(attrs={'class': 'form-input','placeholder': 'ایمیل',}),
            'company_name': forms.TextInput(attrs={'class': 'form-input','placeholder': 'نام شرکت',}),
            'subject': forms.TextInput(attrs= {'class': 'form-input','placeholder': 'موضوع یا دپارتمان',}),
            'message': forms.Textarea(attrs={'class': 'form-input-textarea','placeholder': 'متن پیام'}),
        }
        
        labels = {
            'firstName': '',
            'lastName': '',
            'contact_number': '',
            'email': '',
            'company_name': '',
            'subject': '',
            'message': '',
        }