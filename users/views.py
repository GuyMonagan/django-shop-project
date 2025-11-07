from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserUpdateForm
from .forms import ProfileEditForm

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

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')  # можно редиректить на что угодно
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})
