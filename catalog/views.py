from .models import Product
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'latest_products'
    queryset = Product.objects.filter(is_published=True).order_by('-created_at')[:5]


@method_decorator(cache_page(60), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        product = self.get_object()

        context['can_edit'] = (
            user.is_authenticated and (
                product.owner == user or user.has_perm('catalog.delete_product')
            )
        )
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_unpublish'] = self.request.user.has_perm('catalog.can_unpublish_product')
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Product.objects.all()
        return Product.objects.filter(is_published=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return product.owner == user or user.has_perm('catalog.change_product')


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


    def test_func(self):
        product = self.get_object()
        user = self.request.user

        return product.owner == user or user.has_perm('catalog.delete_product')

    def handle_no_permission(self):
        raise PermissionDenied("Удаление запрещено.")


class ProductUnpublishView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.has_perm('catalog.can_unpublish_product')

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()

        messages.success(request, f'Товар "{product.name}" снят с публикации.')

        return redirect('catalog:product_list')

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для отмены публикации.")


class ProductPublishView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.has_perm('catalog.can_unpublish_product')  # можно использовать те же права

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = True
        product.save()
        messages.success(request, f'Товар "{product.name}" опубликован снова.')
        return redirect('catalog:product_list')

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для публикации товара.")
