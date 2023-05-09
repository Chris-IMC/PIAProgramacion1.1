import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.ebay.com/itm/314566108990?hash=item493d99e73e:g:TWoAAOSw1aBkEihs&amdata=enc%3AAQAIAAAAwJtwRtrw1mjasZ2beXoPlooOk59FH2HCwyFMFfeVET6fz0uO1K9Uk%2FA3%2BTBbh9tDcoYlyBvCB1Fndh1zPrFfWjPLYDh8XUfKuklJ6yBlj5c5D6FnSd%2BdJM2a%2BpNqbyzHcINx71TRYBSSHXL7PJfpmrLlFLhq9BQkStawcIsJtkFvZExguGmW4TYXJPrxBE3sO1pU3NVu2kYCVlOjirBz7DRpkAIzboUwfE30NSer1r%2BNPxzMmuvluQ9mBLquwAWP%2FA%3D%3D%7Ctkp%3ABk9SR5iVhJqAYg'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')

for image in images:
    name = image['alt']
    link = image['src']
    with open(name.replace(' ', '-') + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)
        
       
#link=https://www.youtube.com/watch?v=stIxEKR7o-c&ab_channel=JohnWatsonRooney
