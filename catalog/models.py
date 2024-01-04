from django.contrib.auth import get_user_model
from django.db import models

from users.models import NULLABLE


class BaseContent(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    class Meta:
        abstract = True


class Category(BaseContent):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Service(BaseContent):
    preview = models.ImageField(upload_to='services/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.purchase_price}'

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
        ordering = ('name',)


class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='имя')
    email = models.CharField(max_length=100, verbose_name='email')
    message = models.TextField(verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.full_name} {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Appointment(models.Model):
    TIME_CHOICES = (
        (8, '08:00'),
        (9, '09:00'),
        (10, '10:00'),
        (11, '11:00'),
        (12, '12:00'),
        (13, '13:00'),
        (14, '14:00'),
        (15, '15:00'),
        (16, '16:00'),
        (17, '17:00'),
        (18, '18:00'),
        (19, '19:00'),
        (20, '20:00'),
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, **NULLABLE, verbose_name='услуга')
    date = models.DateField(verbose_name='дата')
    time = models.PositiveSmallIntegerField(choices=TIME_CHOICES, verbose_name='время')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        unique_together = ['service', 'date', 'time']
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('date', 'time')
