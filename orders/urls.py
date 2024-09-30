from django.urls import path

from orders.views import order_view

app_name = 'orders'
urlpatterns = [
    path('create/', order_view, name='create'),
]

