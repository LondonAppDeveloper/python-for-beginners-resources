"""
Weather forecast app.
"""
import argparse
import requests


API_KEY = 'aec7c1999dc9c2ae2cef6f72ff6ef282'
API_BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def handle_args():
    """Handle arguments."""
    parser = argparse.ArgumentParser(description='Forecast the weather.')
    parser.add_argument(
        'city',
        help='Name of city to retrieve data for.'
    )
    parser.add_argument(
        '-u', '--units',
        help='Unit type for values',
        choices=['metric', 'imperial'],
        default='metric'
    )

    return parser.parse_args()


def display_weather(res):
    """Display weather response to use."""
    data = res.json()
    city = data['city']['name']
    country = data['city']['country']
    print(f'Forecast for: {city}, {country}')

    forecast_list = data['list']
    for item in forecast_list:
        print(item['dt_txt'])
        temp = item['main']['temp']
        feels_like = item['main']['feels_like']
        weather = item['weather'][0]['main']
        weather_desc = item['weather'][0]['description']
        print(f' - Temp: {temp}')
        print(f' - Feels like: {feels_like}')
        print(f' - Weather: {weather} - {weather_desc}')


def main():
    """Entrypoint to script."""
    args = handle_args()
    params = {
        'q': args.city, 
        'appid': API_KEY,
        'units': args.units,
    }
    res = requests.get(API_BASE_URL, params=params)
    try:
        res.raise_for_status()
        display_weather(res)
    except requests.exceptions.HTTPError as e:
        print('Unable to retrieve weather.')
        print(e.response.text)


if __name__ == '__main__':
    main()