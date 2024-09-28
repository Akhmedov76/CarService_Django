from django.db import models


class MembersModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members_images')

    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class TestimonialsModel(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
