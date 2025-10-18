from django.contrib import admin
from django.urls import path
from .views import TestOrderAPIView

urlpatterns = [
    path('', TestOrderAPIView.as_view(), name='test-order'),
]
