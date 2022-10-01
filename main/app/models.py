from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название автомобиля')
    about = models.TextField(verbose_name='Описание автомобиля')
    img = models.ImageField(upload_to='media/', verbose_name='Изображение автомобиля')

    def __str__(self):
        return self.name
