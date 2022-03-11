from pyexpat import model
from django.db import models

    
class Weather(models.Model):
    external_id = models.IntegerField()
    main = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    
class CityWeather(models.Model):
    coord = models.JSONField()
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, related_name="weather_condition")
    base = models.CharField(max_length=255)
    temperature = models.JSONField()
    visibility = models.IntegerField()
    wind = models.JSONField()
    clouds = models.JSONField()
    timestamp = models.PositiveBigIntegerField()
    sys = models.JSONField()
    timezone = models.IntegerField()
    external_id = models.IntegerField()
    name = models.CharField(max_length=255)
    cod = models.IntegerField
