from django.db import models


class OrderModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service_type = models.CharField(max_length=255)
    deta = models.DateField(auto_now_add=True)
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
