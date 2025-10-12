from django.views.generic.edit import FormView
from contacts.forms import ContactForm
from contacts.models import ContactData

class ContactView(FormView):
    template_name = "contacts/contacts.html"
    form_class = ContactForm
    success_url = "/contacts/"

    def form_valid(self, form):
        print("Данные формы:", form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = ContactData.objects.all()
        return context