
import os
import requests
from bs4 import BeautifulSoup


google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

saved_folder = 'imagenes'


def main_imagenes():
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)

    download_images()


def download_images():

    data = input('¿Imagenes sobre qué buscas? ')
    n_images = int(input('¿Cuantas imagenes quieres? '))

    print('Buscando...')

    search_url = google_image + 'q=' + data

    response = requests.get(search_url, headers=user_agent,)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    count = 1
    links = []
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            count += 1
            if(count > n_images):
                break

        except KeyError:
            continue

    print(f"Descargando {len(links)} Imagenes...")
    print("Hecho, las guardé en la carpeta 'imagenes'")
    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + '/' + data + str(i+1) + '.jpg'

        with open(image_name, 'wb') as fh:
            fh.write(response.content)
    input("Presiona ENTER Para continuar...")




if __name__ == "__main__":
    main_imagenes()

