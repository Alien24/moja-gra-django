import os
from django.core.wsgi import get_wsgi_application

# Tutaj nazwa folderu z ustawieniami – u Ciebie hello_django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

application = get_wsgi_application()