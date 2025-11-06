from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.core.mail import send_mail

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            'Добро пожаловать!',
            f'Привет, {self.object.email}! Вы успешно зарегистрировались.',
            'noreply@example.com',
            [self.object.email],
            fail_silently=True,
        )
        return response

