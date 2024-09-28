from django.shortcuts import render

from .models import AboutModel, BannersModel, ServicesModel
from teams.models import MembersModel, TestimonialsModel


def home_page_view(request):
    about = AboutModel.objects.all()
    banners = BannersModel.objects.all()
    services = ServicesModel.objects.all()
    teams = MembersModel.objects.all()
    testimonials = TestimonialsModel.objects.all()

    context = {
        'about': about,
        'banners': banners,
        'services': services,
        'members': teams,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)


def about_page_view(request):
    return render(request, 'about.html')


def booking_page_view(request):
    return render(request, 'booking.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def service_page_view(request):
    return render(request, 'service.html')


def team_page_view(request):
    teams = MembersModel.objects.all()
    context = {'teams': teams}
    return render(request, 'team.html')


def testimonial_page_view(request):
    return render(request, 'testimonial.html')


def error_page_view(request):
    return render(request, '404.html')
