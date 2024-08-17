import requests
from datetime import datetime

API_KEY = '9de303f7f5123a36fc14d38a060cde6e'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

def get_weather(city):
    try:
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'pt_br'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f'Erro na requisição: {err}')
        return None

def display_weather(weather_data):
    for entry in weather_data['list']:
        date_time = entry['dt_txt']
        temperature = entry['main']['temp']
        description = entry['weather'][0]['description']
        print(f'{date_time}: {temperature}°C, {description.capitalize()}')

def get_specific_date_weather(weather_data, date):
    for entry in weather_data['list']:
        if date in entry['dt_txt']:
            temperature = entry['main']['temp']
            description = entry['weather'][0]['description']
            print(f'{entry["dt_txt"]}: {temperature}°C, {description.capitalize()}')

def main():
    while True:
        print("\n--- Verificador de Meteorologia ---")
        city = input('Digite o nome da cidade: ')
        weather_data = get_weather(city)
        
        if weather_data:
            print("\n1. Ver previsão para a semana")
            print("2. Ver previsão para uma data específica")
            option = input('Escolha uma opção (1 ou 2): ')
            
            if option == '1':
                display_weather(weather_data)
            elif option == '2':
                date = input('Digite a data no formato YYYY-MM-DD: ')
                get_specific_date_weather(weather_data, date)
            else:
                print("Opção inválida. Tente novamente.")
        
        repeat = input('\nDeseja fazer outra consulta? (s/n): ').lower()
        if repeat != 's':
            break

if __name__ == "__main__":
    main()
