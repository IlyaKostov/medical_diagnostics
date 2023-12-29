from django import forms

from catalog.models import Service, Category, Appointment


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
