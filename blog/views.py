from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Показываем только опубликованные статьи
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()

        if obj.views_count == 100:
            send_mail(
                subject='Поздравляем! 🎉',
                message=f'Статья "{obj.title}" набрала 100 просмотров!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,
            )

        return obj


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

