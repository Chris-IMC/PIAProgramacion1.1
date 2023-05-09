import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.buenamusica.com/'

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def main_noti():

    download_noti()

def download_noti():

    data = input('¿Sobre qué Artista/Grupo buscas información? ')

    search_url = url + data + '/noticias'

    response = requests.get(search_url, headers=user_agent, )

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')


    acer = soup.find_all('div', {'class': 'col-22 col-xs-24 noticia-inner'})

    noticias = list()

    count = 0
    for i in acer:
        if count < 20:
            noticias.append(i.get_text('https://www.buenamusica.com/' + data + '/noticias' ))
        else:
            break
        count += 1
    print(noticias)

    df = pd.DataFrame({'nombre':noticias})
    df.to_csv('Noticias.csv', index=False)
    print(df)

    archivo = open("noticias.txt","w")
    archivo.write(str((noticias)))
    archivo.close()

if __name__ == "__main__":
    main_noti()
