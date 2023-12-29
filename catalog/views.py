from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

from catalog.forms import CategoryForm
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


class CategoryDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Category


class CategoryListView(LoginRequiredMessageMixin, PermissionRequiredMixin, ListView):
    model = Category


class CategoryDetailView(LoginRequiredMessageMixin, PermissionRequiredMixin, DetailView):
    model = Category


class ServiceCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Service
    # form_class = MailingForm
    # permission_required = 'mailing_service.add_mailing'
    # success_url = reverse_lazy('mailing_service:mailing_list')

    # def get_form(self, form_class=None):
    #     """Формирование полей 'clients' и 'message' в форме, принадлежащих текущему пользователю"""
    #     form = super().get_form(form_class)
    #     form.fields['clients'].queryset = Client.objects.filter(user=self.request.user)
    #     form.fields['message'].queryset = Message.objects.filter(user=self.request.user)
    #     return form


class ServiceUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Service
    # form_class = MailingForm
    # permission_required = 'mailing_service.change_mailing'

    def get_success_url(self):
        return reverse('mailing_service:mailing_detail', args=[self.kwargs.get('pk')])


class ServiceListView(LoginRequiredMessageMixin, PermissionRequiredMixin, ListView):
    model = Service
    # permission_required = 'mailing_service.view_mailing'


class ServiceDetailView(LoginRequiredMessageMixin, PermissionRequiredMixin, DetailView):
    model = Service
    # permission_required = 'mailing_service.view_mailing'


class ServiceDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Service
    # permission_required = 'mailing_service.delete_mailing'
    # success_url = reverse_lazy('mailing_service:mailing_list')


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
