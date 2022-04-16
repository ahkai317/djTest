"""
WSGI config for ideTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ideTest.settings')

application = get_wsgi_application()

# sys.path.append('C:\\Users\\Administrator\\All_studies_for_coding\\WEB_studies\\django\\ideTest\\')
# sys.path.append('C:\\Users\\Administrator\\pythonEnvs\\envs\\django_test\\Lib\\site-packages\\django\\bin')
# sys.path.append('C:\\Users\\Administrator\\pythonEnvs\\envs\\django_test\\Scripts\\')
