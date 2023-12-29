from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

from catalog.forms import CategoryForm, ServiceForm
from catalog.models import Service, Category, Appointment


class HomePageView(TemplateView):
    template_name = "catalog/index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["latest_articles"] = Article.objects.all()[:5]
    #     return context


class LoginRequiredMessageMixin(LoginRequiredMixin):
    """Ограничение доступа только для авторизованных пользователей, вывод соответствующего информационного сообщения"""

    def handle_no_permission(self):
        messages.error(self.request, 'Для доступа к этой странице необходимо авторизоваться')
        return super().handle_no_permission()


class CategoryCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Category
    permission_required = 'catalog.add_category'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    permission_required = 'catalog.change_category'

    def get_success_url(self):
        return reverse('catalog:category', args=[self.kwargs.get('pk')])


class CategoryDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    permission_required = 'catalog.delete_category'
    success_url = reverse_lazy('catalog:category_list')


class CategoryListView(LoginRequiredMessageMixin, PermissionRequiredMixin, ListView):
    model = Category
    permission_required = 'catalog.view_category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryDetailView(LoginRequiredMessageMixin, PermissionRequiredMixin, DetailView):
    model = Category
    permission_required = 'catalog.view_category'


class ServiceCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    permission_required = 'catalog.add_service'
    success_url = reverse_lazy('catalog:service_list')

    # def get_form(self, form_class=None):
    #     """Формирование полей 'clients' и 'message' в форме, принадлежащих текущему пользователю"""
    #     form = super().get_form(form_class)
    #     form.fields['clients'].queryset = Client.objects.filter(user=self.request.user)
    #     form.fields['message'].queryset = Message.objects.filter(user=self.request.user)
    #     return form


class ServiceUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    permission_required = 'catalog.change_service'

    def get_success_url(self):
        return reverse('catalog:service', args=[self.kwargs.get('pk')])


class ServiceListView(LoginRequiredMessageMixin, PermissionRequiredMixin, ListView):
    model = Service
    permission_required = 'catalog.view_service'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ServiceDetailView(LoginRequiredMessageMixin, PermissionRequiredMixin, DetailView):
    model = Service
    permission_required = 'catalog.view_service'


class ServiceDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Service
    permission_required = 'catalog.delete_service'
    success_url = reverse_lazy('catalog:service_list')


class AppointmentCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Appointment


class AppointmentDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Appointment


class AppointmentUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Appointment


class AppointmentDetailView(LoginRequiredMessageMixin, PermissionRequiredMixin, DetailView):
    model = Appointment


class AppointmentListView(LoginRequiredMessageMixin, PermissionRequiredMixin, ListView):
    model = Appointment
