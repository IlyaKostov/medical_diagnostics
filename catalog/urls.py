from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomePageView, CategoryListView, CategoryDetailView, CategoryDeleteView, CategoryCreateView, \
    CategoryUpdateView, ServiceListView, ServiceDetailView, ServiceDeleteView, ServiceUpdateView, ServiceCreateView, \
    AppointmentListView, AppointmentDetailView, AppointmentDeleteView, AppointmentUpdateView, AppointmentCreateView, \
    ContactView, AboutUs

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/service/', ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
    path('service/update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('service/create/', ServiceCreateView.as_view(), name='service_create'),
    path('appointment/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('appointment/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutUs.as_view(), name='about'),
]
