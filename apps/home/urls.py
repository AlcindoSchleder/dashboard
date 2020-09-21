# -*- coding: utf-8 -*-
from django.urls import path
from .views import DashboardView

app_name = 'home'
urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    # path('graph/', ShowGraphView.as_view(), name='graphs'),
]