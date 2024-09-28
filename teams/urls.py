from django.urls import path

from .views import home_view

urlpatterns = [
    path('team/', home_view, name='home'),
]
