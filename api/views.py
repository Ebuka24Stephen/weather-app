from django.shortcuts import render
import requests
import json
from django.conf import settings
def index(request):
    try:
        city = request.GET.get('city')
        API_KEY = settings.API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url).json()

        weather_data = {
            'city': city,
            'description': response['weather'][0]['description'],
            'wind': response['wind']['speed'],
            'temperature': response['main']['temp'] - 273.15  
        }

        return render(request, 'home.html', {'weather_data': weather_data})

    except requests.exceptions.RequestException as e:
        error_message = f"Error retrieving weather data: {str(e)}"
        return render(request, 'home.html', {'error': error_message})

    except KeyError:
        error_message = "Error: Could not find weather data for the specified city."
        return render(request, 'home.html', {'error': error_message})

    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return render(request, 'home.html', {'error': error_message})
