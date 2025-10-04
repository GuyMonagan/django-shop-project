from django.shortcuts import render
from .forms import ContactForm
from .models import ContactData

def contacts_view(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Данные формы:", form.cleaned_data)
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    contacts = ContactData.objects.all()

    return render(request, "contacts/contacts.html", {
        "form": form,
        "success": success,
        "contacts": contacts,
    })
