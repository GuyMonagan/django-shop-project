from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone', 'country')

class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)
