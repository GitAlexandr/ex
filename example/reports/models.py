from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новое'),
        ('confirmed', 'Подтверждено'),
        ('rejected', 'Отклонено'),
    )
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.title} #{self.pk} - {self.car_number}"