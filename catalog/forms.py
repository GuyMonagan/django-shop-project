from django import forms
from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)

# Запрещённые слова
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # Чекбокс на всякий случай
        if 'some_boolean_field' in self.fields:
            self.fields['some_boolean_field'].widget.attrs.update({'class': 'form-check-input'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if any(forbidden in name.lower() for forbidden in FORBIDDEN_WORDS):
            raise forms.ValidationError("Название содержит запрещённые слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if any(forbidden in description.lower() for forbidden in FORBIDDEN_WORDS):
            raise forms.ValidationError("Описание содержит запрещённые слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


def clean_image(self):
    image = self.cleaned_data.get('image')
    if image:
        if hasattr(image, 'content_type'):
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Только JPEG и PNG изображения поддерживаются.")
        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Размер файла не должен превышать 5 МБ.")
    return image
