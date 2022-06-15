from .models import ArticlesComments
from django import forms


class SubmitComment(forms.ModelForm):
    class Meta:
        model = ArticlesComments
        fields = ['first_name', 'last_name', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'نام', }),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی', }),
            'comment': forms.Textarea(attrs={'placeholder': 'متن پیام', }),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'comment': '',
        }