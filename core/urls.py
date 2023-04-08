# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) © Atos SE 2023 all rights reserved
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls"))  # add this
]
