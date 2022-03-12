from rest_framework.exceptions import APIException
from django.conf import settings
import requests


class WeatherMapClient:
    base_url = "http://api.openweathermap.org/data/2.5"
    api_key = settings.WEATHERMAP_API_KEY
    units = "metric"
    
    @classmethod
    def get_weather_by_city(self, city: str = "Warsaw"):
        resource_url = self.base_url + "/weather"
        query_params = {
            "q": city,
            "units": self.units,
            "appid": self.api_key
        }
        try:
            request = requests.get(resource_url, params=query_params)
        except requests.exceptions.RequestException as e:
            raise APIException(e)
        return request.json()