from rest_framework import viewsets, status
from rest_framework.response import Response
from weather_app_client.models import CityWeather
from weather_app_client.serializers import CityWeatherSerializer
from weather_app_client.weathermap_client import WeatherMapClient


class CityWeatherView(viewsets.ViewSet):
    
    def create(self, request):
        weather_data = WeatherMapClient.get_weather_by_city("Warsaw")
        serializer = CityWeatherSerializer(data=weather_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result":"Weather data collected"}, status=status.HTTP_200_OK)
        return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def list(self, request):
        queryset = CityWeather.objects.all()
        # print(queryset[0].weather)
        serializer = CityWeatherSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)