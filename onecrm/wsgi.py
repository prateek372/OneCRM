"""
WSGI config for djcrm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onecrm.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  #added SO
django.setup()

# import django     #added SO
# django.setup()   #added SO

application = get_wsgi_application()

