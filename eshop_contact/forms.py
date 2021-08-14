from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی', 'class': 'form-control'}),
        label='نام و نام خانوادگی',

    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'form-control'}),
        label='ایمیل',
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'عنوان پیام', 'class': 'form-control'}),
        label='عنوان پیام',

    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام', 'class': 'form-control', 'rows': '8'}),
        label='متن پیام'
    )
