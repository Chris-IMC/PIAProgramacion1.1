from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


url = 'https://www.ticketmaster.com.mx/search?'
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def main_even():

    download_even()

def download_even():
    data = input('¿Fechas próximas de qué grupo/artista/evento estás buscando? ')

    search_url = url + 'q=' + data
    response = requests.get(search_url, headers=user_agent, )
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

#Día_Semana
    ep = soup.find_all('span', class_='sc-1d1xejb-1 bfImhh')

    Día_Semana = list()

    count = 0
    for i in ep:
        if count < 20:
            Día_Semana.append(i.text)
        else:
            break
        count += 1
    print(Día_Semana)


    # Ubicacion
    eq = soup.find_all('span', class_='sc-1y6w6fq-4 jtSGIy')

    Ubicacion = list()

    count = 0
    for i in eq:
        if count < 20:
            Ubicacion.append(i.text)
        else:
            break
        count += 1
    print(Ubicacion)

    # FECHA
    er = soup.find_all('div', class_='sc-1vjs9rz-1 CfMhK')

    fecha = list()

    count = 0
    for i in er:
        if count < 20:
            fecha.append(i.text)
        else:
            break
        count += 1
    print(fecha)

    # Día
    es = soup.find_all('div', class_='sc-1vjs9rz-2 fJHqHk')

    Día = list()

    count = 0
    for i in es:
        if count < 20:
            Día.append(i.text)
        else:
            break
        count += 1
    print(Día)

    # Hora
    et = soup.find_all('span', class_='sc-1d1xejb-2 jfgVSr')

    Hora = list()

    count = 0
    for i in et:
        if count < 20:
            Hora.append(i.text)
        else:
            break
        count += 1
    print(Hora)

    # Artista
    eu = soup.find_all('span', class_='sc-1y6w6fq-3 fBQxZv')

    Artista = list()

    count = 0
    for i in eu:
        if count < 20:
            Artista.append(i.text)
        else:
            break
        count += 1
    print(Artista)


    df = pd.DataFrame({'Mes':fecha,'Día':Día,'Día(Semana)':Día_Semana,'Hora':Hora,'Ubicación':Ubicacion,'Artista':Artista})
    df.to_csv ('Fechas.csv', index=False)
    input("Listo, guardé las fechas en un archivo exel, presiona ENTER Para continuar...")

    archivo = open("fechas.txt","w")
    for linea in Ubicacion:
        archivo.write(linea + "\n")
    archivo.close()

if __name__ == "__main__":
    main_even()


