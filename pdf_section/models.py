from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Town(models.Model):
    name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)

    class Meta:
        ordering = ['county', 'name']

    def __str__(self):
        return self.name


class Weather(models.Model):
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    description = models.TextField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    wind_speed = models.IntegerField(validators=[MinValueValidator(0)])
    precipitation = models.IntegerField()
    precipitation_probability = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    observations = models.TextField()

    class Meta:
        unique_together = ('town', 'date')
        ordering = ['-date', 'town']

    def __str__(self):
        dtos = self.date.strftime('%d-%m-%Y')
        return self.town.name + " " + dtos
