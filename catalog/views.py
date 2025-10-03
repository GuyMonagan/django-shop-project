from django.shortcuts import render
from .forms import ContactForm
from .models import Product, ContactData

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'catalog/home.html', {'latest_products': latest_products})

def contacts_view(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Данные формы:", form.cleaned_data)
            success = True
            form = ContactForm()  # очищаем форму
    else:
        form = ContactForm()

    contacts = ContactData.objects.all()

    return render(request, "catalog/contacts.html", {
        "form": form,
        "success": success,
        "contacts": contacts,
    })
