from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

from catalog.forms import CategoryForm, ServiceForm, AppointmentForm, FeedbackForm
from catalog.models import Service, Category, Appointment, Contact
from catalog.services import get_random_blog_article


class HomePageView(TemplateView):
    template_name = "catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_article'] = get_random_blog_article()
        context['categories'] = Category.objects.order_by('?')[:4]
        context['services'] = Service.objects.order_by('?')[:3]
        return context


class LoginRequiredMessageMixin(LoginRequiredMixin):
    """Ограничение доступа только для авторизованных пользователей, вывод соответствующего информационного сообщения"""

    def handle_no_permission(self):
        messages.error(self.request, 'Для доступа к этой странице необходимо авторизоваться')
        return super().handle_no_permission()


class UserObjectMixin:
    """Ограничивает доступ пользователя к чужим объектам"""
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class CategoryCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Category
    permission_required = 'catalog.add_category'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'catalog.change_category'

    def get_success_url(self):
        return reverse('catalog:category', args=[self.kwargs.get('pk')])


class CategoryDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    permission_required = 'catalog.delete_category'
    success_url = reverse_lazy('catalog:category_list')


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ServiceCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    permission_required = 'catalog.add_service'
    success_url = reverse_lazy('catalog:service_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ServiceUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    permission_required = 'catalog.change_service'

    def get_success_url(self):
        return reverse('catalog:service', args=[self.kwargs.get('pk')])


class ServiceListView(ListView):
    model = Service

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ServiceDetailView(DetailView):
    model = Service


class ServiceDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, DeleteView):
    model = Service
    permission_required = 'catalog.delete_service'
    success_url = reverse_lazy('catalog:category_list')


class AppointmentCreateView(LoginRequiredMessageMixin, PermissionRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    permission_required = 'catalog.add_appointment'
    success_url = reverse_lazy('catalog:appointment_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AppointmentDeleteView(LoginRequiredMessageMixin, PermissionRequiredMixin, UserObjectMixin, DeleteView):
    model = Appointment
    permission_required = 'catalog.delete_appointment'
    success_url = reverse_lazy('catalog:appointment_list')


class AppointmentUpdateView(LoginRequiredMessageMixin, PermissionRequiredMixin, UserObjectMixin, UpdateView):
    model = Appointment
    permission_required = 'catalog.change_appointment'
    form_class = AppointmentForm
    success_url = reverse_lazy('catalog:appointment_list')


class AppointmentDetailView(LoginRequiredMessageMixin, PermissionRequiredMixin, UserObjectMixin, DetailView):
    model = Appointment
    permission_required = 'catalog.view_appointment'


class AppointmentListView(LoginRequiredMessageMixin, PermissionRequiredMixin, ListView):
    model = Appointment
    permission_required = 'catalog.view_appointment'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(date__gte=datetime.today())
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)


class ContactView(CreateView):
    template_name = 'catalog/contact.html'
    form_class = FeedbackForm
    model = Contact
    success_url = reverse_lazy('catalog:contact')


class AboutUs(TemplateView):
    template_name = 'catalog/about_us.html'
