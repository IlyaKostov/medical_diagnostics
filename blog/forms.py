from django import forms

from blog.models import Blog
from users.forms import FormClassMixin


class BlogForm(FormClassMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            "title",
            "category",
            "content",
            "preview",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Введите заголовок",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Напишите текст поста",
                }
            )
        }
