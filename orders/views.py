from django.shortcuts import render, redirect

from orders.forms import OrderModelForm
from services.models import BannersModel, ServicesModel
from teams.models import MembersModel, TestimonialsModel


def order_view(request):
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')
