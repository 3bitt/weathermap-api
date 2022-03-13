import pytest
from weather_app_client.serializers import CityWeatherSerializer


@pytest.mark.django_db
class TestCityWeatherSerializer:
    
    def test_serialize_model(self, city_weather_db_mock):
        serializer = CityWeatherSerializer(city_weather_db_mock)
        assert serializer.data
        
    def test_serialize_data(self, city_weather_service_mock):
        data = city_weather_service_mock.return_value
        serializer = CityWeatherSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.errors == {}
        