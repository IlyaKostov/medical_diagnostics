import os

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        os.system("python manage.py loaddata blog.json")
        os.system("python manage.py loaddata catalog.json")
