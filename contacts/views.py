from django.views.generic.edit import FormView
from contacts.forms import ContactForm
from contacts.models import ContactData
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm  # форма редактирования, создадим ниже

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})


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