from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.full_name()
