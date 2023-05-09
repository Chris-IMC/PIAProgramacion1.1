import requests
from io import open
import json
import math

def main_clima():
    clima()


def clima():

    archivo_texto = open('Ubicacion de eventos.txt','r')
    texto=archivo_texto.readlines()
    archivo_texto.close()
    print(texto)


    for i in texto:
        api_address= 'http://api.openweathermap.org/data/2.5/weather?appid=64f44b4cf75adb58e6b9881ac6f4bc4c&q='
        city = i
        url = api_address + city
        json_data = requests.get(url).json()
        formatted_data = json_data['main']['temp']
        listas=formatted_data
        grados= math.floor(formatted_data-273.15)
        print(f'La temperatura de',i,'es',grados,'℃')

if __name__ == "__main__":
    main_clima()

    

