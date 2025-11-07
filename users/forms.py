from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'avatar', 'phone', 'country', 'password1', 'password2')

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar', 'phone', 'country']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'country': forms.TextInput(attrs={'placeholder': 'Страна'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'avatar', 'phone', 'country']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }
