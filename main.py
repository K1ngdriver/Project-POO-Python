import requests

API_KEY = '9de303f7f5123a36fc14d38a060cde6e'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city):
    try:
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric', 'lang': 'pt_br'})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f'Erro na requisição: {err}')
        return None

def print_header(title):
    print(f"\n{'-'*len(title)}")
    print(title)
    print(f"{'-'*len(title)}\n")

def display_weather(weather_data):
    print_header("Previsão para a Semana")
    print(f"{'Data e Hora':^20} | {'Temperatura (°C)':^20} | {'Descrição':^30}")
    print("-"*72)
    for entry in weather_data['list']:
        date_time = entry['dt_txt']
        temperature = entry['main']['temp']
        description = entry['weather'][0]['description'].capitalize()
        print(f"{date_time:^20} | {temperature:^20} | {description:^30}")
    print("-"*72)

def get_specific_date_weather(weather_data, date):
    print_header(f"Previsão para {date}")
    found = False
    for entry in weather_data['list']:
        if date in entry['dt_txt']:
            found = True
            date_time = entry['dt_txt']
            temperature = entry['main']['temp']
            description = entry['weather'][0]['description'].capitalize()
            print(f"{'Data e Hora':^20} | {'Temperatura (°C)':^20} | {'Descrição':^30}")
            print("-"*72)
            print(f"{date_time:^20} | {temperature:^20} | {description:^30}")
            print("-"*72)
    if not found:
        print("Nenhuma previsão encontrada para a data especificada.")

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
