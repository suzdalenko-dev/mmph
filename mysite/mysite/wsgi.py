"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/


PERPLEXITI > COMET maneja su brouser desde texto

CLAUDE COWORK - agente que vive en tu ordenador y puede hacer lo que hay que hacer con palabras,
puede manejar PC, solo USA y en MAC

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
