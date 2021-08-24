from django import forms
from django.contrib.auth.models import User


class EditProfileForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام', 'class': 'form-control'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'class': 'form-control'}),
        label='نام خانوادگی'
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        label='کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_user_exist = User.objects.filter(username=user_name).exists()

        if not is_user_exist:
            raise forms.ValidationError('کاربری با این مشخصات ثبت نام نکرده است')
        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        label='ایمیل'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        label='کلمه عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'}),
        label='تکرار کلمه عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_exist_by_email = User.objects.filter(email=email).exists()

        if user_exist_by_email:
            raise forms.ValidationError('این ایمیل قبلا استفاده شده است')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        user_exist_by_username = User.objects.filter(username=user_name).exists()

        if user_exist_by_username:
            raise forms.ValidationError('کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')
        return password
