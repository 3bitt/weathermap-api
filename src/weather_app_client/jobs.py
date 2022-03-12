from weather_app_client.serializers import CityWeatherSerializer
from weather_app_client.weathermap_client import WeatherMapClient


def fetch_weather_data():
    weather_data = WeatherMapClient.get_weather_by_city("Warsaw")
    serializer = CityWeatherSerializer(data=weather_data)
    if serializer.is_valid():
        serializer.save()
