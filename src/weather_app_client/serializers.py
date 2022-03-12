from rest_framework import serializers
from weather_app_client.models import CityWeather, WeatherDetail


class WeatherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="external_id")
    class Meta:
        model = WeatherDetail
        fields = [
            "id",
            "main",
            "description",
            "icon"
        ]


class CityWeatherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="external_id")
    weather = WeatherSerializer(many=True, required=False)
    class Meta:
        model = CityWeather
        fields = [
            "coord",
            "weather",
            "base",
            "main",
            "visibility",
            "wind",
            "clouds",
            "dt",
            "sys",
            "timezone",
            "id",
            "name",
            "cod",
            "timestamp"
        ]
        
    def create(self, validated_data: dict):
        weather = validated_data.pop("weather")
        city_weather = CityWeather.objects.create(**validated_data)
        for item in weather:
            WeatherDetail.objects.create(city_weather=city_weather, **item)
        return city_weather