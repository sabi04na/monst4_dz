from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    age = models.IntegerField(verbose_name="Возраст")
    city = models.CharField(max_length=50, verbose_name="Город")
    profession = models.CharField(max_length=100, verbose_name="Профессия")
    skills = models.TextField(verbose_name="Навыки")
    about = models.TextField(verbose_name="О себе")

    def __str__(self):
        return self.full_name
