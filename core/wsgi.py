# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) © Atos SE 2023 all rights reserved
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
