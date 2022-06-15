from customizedUserModel.models import Userperson
from django import forms

gender_choice = [
    ('male', 'male'),
    ('female', "female")
]
roles = [
    ('user', 'user'),
    ('seller', 'seller'),
    ('service', 'service'),
    ('admin', 'admin'),
]

class RegisterForm(forms.ModelForm):
    class Meta:
        fields = ['fullname','phone','image','address','gender','password']
        model = Userperson

    def clean(self):
        if str(self.cleaned_data.get('phone')).isdigit() and len(str(self.cleaned_data.get('phone'))) ==11:
            if str(self.cleaned_data.get('image')).split('.')[::-1][0] not in  ['html','php','js','py','css']:
                return self.cleaned_data
            else:
                return forms.ValidationError('فرمت عکس ارسال شده پشتیبانی نمیشود')
        else:
            raise forms.ValidationError('شماره تلفن باید عدد باشد و ۱۱ رقم باشد')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs.update({'class': 'login-inp','placeholder': 'نام و نام خانوداگی'})
        self.fields['phone'].widget.attrs.update({'class': 'login-inp','placeholder': '09123213213'})
        self.fields['image'].widget.attrs.update({'class': 'login-inp'})
        self.fields['address'].widget.attrs.update({'class': 'login-inp'})
        self.fields['gender'].widget.attrs.update({'class': 'login-inp'})
        self.fields['password'].widget.attrs.update({'class': 'login-inp','placeholder': '*********'})
        self.fields['fullname'].required = True
        self.fields['phone'].required = True
        self.fields['image'].required = True
        self.fields['address'].required = True
        self.fields['gender'].required = True
        self.fields['password'].required = True