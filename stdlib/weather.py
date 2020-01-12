import json
import urllib.request

def main():
    lokalizacja = input('Podaj lokalizację: ')
    url = 'https://www.metaweather.com/api/location/search/?query=' + lokalizacja
    with urllib.request.urlopen(url) as r:
        data = r.read()

    found_locations = json.loads(data)
    if not found_locations:
        print("Nie znaleziono takiej lokalizacji")
        return
    woeid = found_locations[0]['woeid']

    url = f'https://www.metaweather.com/api/location/{woeid}/'
    with urllib.request.urlopen(url) as r:
        data = r.read()

    weather_today = json.loads(data)['consolidated_weather'][0]
    print(f'Temperatura: {weather_today["the_temp"]:.2f} C')
    print(f'Ciśnienie: {weather_today["air_pressure"]} hPa')
    print(f'Wiatr: {round(weather_today["wind_speed"]*1.6,2)} kmh')

if __name__ == '__main__':
    main()