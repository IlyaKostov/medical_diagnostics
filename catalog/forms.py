from django import forms

from catalog.models import Service, Category, Appointment, Contact
from users.forms import FormClassMixin


class ServiceForm(FormClassMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class CategoryForm(FormClassMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AppointmentForm(FormClassMixin, forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ('user',)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }


class FeedbackForm(FormClassMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

