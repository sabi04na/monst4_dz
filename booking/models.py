from django.db import models
from horse_tours.models import Person, TourCompany, Service

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание подтверждения'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отменена'),
    ]

    
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Клиент",
        related_name="bookings"
    )
    company = models.ForeignKey(
        TourCompany,
        on_delete=models.CASCADE,
        verbose_name="Тур-компания",
        related_name="bookings"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        verbose_name="Услуга",
        related_name="bookings"
    )

    # Дополнительные поля
    booking_date = models.DateField(verbose_name="Дата тура")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Статус"
    )
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.person.name} — {self.company.name} ({self.booking_date})"
