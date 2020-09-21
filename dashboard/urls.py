# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('fontawesome/', include("django_static_fontawesome.urls")),
    path('', include('apps.home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
