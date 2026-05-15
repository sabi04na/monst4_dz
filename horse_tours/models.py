from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name


class Horse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя лошади")
    breed = models.CharField(max_length=100, verbose_name="Порода")
    owner = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="horse"
    )

    def __str__(self):
        return self.name

class TourCompany(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name


class Review(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="Автор отзыва",
        related_name="reviews"
    )
    company = models.ForeignKey(
        TourCompany,
        on_delete=models.CASCADE,
        verbose_name="Компания",
        related_name="reviews"
    )
    text = models.TextField(verbose_name="Отзыв")
    rating = models.IntegerField(
        verbose_name="Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.person.name} → {self.company.name} ({self.rating}/5)"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    companies = models.ManyToManyField(
        TourCompany,
        verbose_name="Компании",
        related_name="services"
    )

    def __str__(self):
        return self.name
