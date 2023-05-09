from PIL import Image
import io
import requests
from bs4 import BeautifulSoup as b
import win32api

url = 'https://www.soriana.com/?gclid=CjwKCAjw3ueiBhBmEiwA4BhspKKPqqdFcVwYYuztKF-ccq-yMO4YVfrU8faoGosOUyaXsKonDK0RzxoCYwoQAvD_BwE'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept-Encoding":"gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT":"1"
}

ruta_imagenes = r'C:\Python\DEBER1PYTHON\PROGRAMACION PIA\imagenes'

html= requests.get(url,headers=headers)
content = html.content
soup = b(content,"lxml")
i= 1
for post in soup.findAll('div',{"class":"product-item"}):

    title = post.find('h2',{"class":"product-title"}).text

    url_img = post.find('img')['data-src']

    r = requests.get(url_img)

    file = io.BytesIO(r.content)

    img = Image.open(file)

    img.save(ruta_imagenes+"\\"+str(title)+".jpg")
    print(i)
    i += 1

win32api.MessageBox(False,'Hecho se guardaron las imagenes', 'Finalizado', 0x00001000)

