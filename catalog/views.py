from django.shortcuts import render
from .forms import ContactForm

def home_view(request):
    return render(request, "catalog/home.html")

def contacts_view(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Здесь можно было бы обработать данные формы
            print("Данные формы:", form.cleaned_data)
            success = True
            form = ContactForm()  # очищаем форму
    else:
        form = ContactForm()

    return render(request, "catalog/contacts.html", {"form": form, "success": success})
