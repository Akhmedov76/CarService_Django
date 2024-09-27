from django.contrib import admin

from .models import CustomerModel, CarModel, ServiceModel, Service

admin.site.register(CustomerModel)
admin.site.register(CarModel)
admin.site.register(ServiceModel)
admin.site.register(Service)
