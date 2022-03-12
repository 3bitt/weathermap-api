from django.db import models

    
class CityWeather(models.Model):
    coord = models.JSONField()
    base = models.CharField(max_length=255)
    main = models.JSONField()
    visibility = models.IntegerField()
    wind = models.JSONField()
    clouds = models.JSONField()
    dt = models.PositiveBigIntegerField()
    sys = models.JSONField()
    timezone = models.IntegerField()
    external_id = models.IntegerField()
    name = models.CharField(max_length=255)
    cod = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)


class WeatherDetail(models.Model):
    external_id = models.IntegerField()
    main = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    city_weather = models.ForeignKey(CityWeather, on_delete=models.CASCADE, related_name="weather")