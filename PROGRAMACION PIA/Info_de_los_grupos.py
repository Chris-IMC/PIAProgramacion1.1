from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.buenamusica.com/'

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def main_info():

    download_info()

def download_info():

    data = input('¿Sobre qué Artista/Grupo buscas información? ')

    search_url = url + data + '/biografia'

    response = requests.get(search_url, headers=user_agent, )

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    acercade = soup.find_all('div', {'class': 'biografia-textoOld ArticleTextDiv'})[0].get_text()

    print(acercade)

    archivo = open("acerca_de.txt","w")
    archivo.write(str((acercade)))
    archivo.close()

if __name__ == "__main__":
    main_info()







