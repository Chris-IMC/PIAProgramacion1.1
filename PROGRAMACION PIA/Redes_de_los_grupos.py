from bs4 import BeautifulSoup as bs
from googlesearch import search
import requests, re, os, time

def main_redes():

    download_redes()

def download_redes():

  search_query = input('Introduce la banda a buscar informacion: ')


  resultados_GS = open('resultados_Busqueda.txt', 'w')
  for i in search(search_query, tld='com', lang='es',  num=10, stop=10,pause=10.0,extra_params={'filter': '0'}):
      resultados_GS.write(i+'\n')
  resultados_GS.close()

  lectura1 = open('resultados_Busqueda.txt', 'r')
  lineas_rB = lectura1.readlines()
  lectura1.close()

  html_GS = ['resultado_B-1.html', 'resultado_B-2.html', 'resultado_B-3.html', 'resultado_B-4.html', 'resultado_B-5.html',
            'resultado_B-6.html', 'resultado_B-7.html', 'resultado_B-8.html', 'resultado_B-9.html', 'resultado_B-10.html']

  urls_rB = open('resultados_B-URLs.txt', 'w')
  urls_rB.close()

  for i in range(len(lineas_rB)):
    page = requests.get(lineas_rB[i])
    #print (page.status_code)            ##200 = 'ok'

    urls = bs(page.text, 'html.parser')
    html_URLs = urls.find_all('a')
    for url in html_URLs:
      urls_rB = open('resultados_B-URLs.txt', 'a')
      urls_rB.write(str(url.get('href'))+'\n')

      soup_GS = bs(page.content, 'html.parser')

      resultados_HTML = open (html_GS[i], 'w', encoding='UTF-8')
      resultados_HTML.write (str(soup_GS.prettify()))
    urls_rB.close()
  i=i+1
  time.sleep(3)
  resultados_HTML.close()

  ##Expresiones regulares
  patron_FB = re.compile(rf'http://www\.facebook\.com/{search_query}\w+|https://www\.facebook\.com/{search_query}\w+|www\.facebook\.com/{search_query}\w+')
  patron_TWT = re.compile(rf'http://www\.twitter\.com/{search_query}\w+|https://www\.twitter\.com/{search_query}\w+|www\.twitter\.com/{search_query}\w+')
  patron_IG = re.compile(rf'http://www\.instagram\.com/{search_query}\w+|https://www\.instagram\.com/{search_query}\w+|www\.instagram\.com/{search_query}\w+')

  lectura2 = open('resultados_B-URLs.txt', 'r')
  lineas_htmls = lectura2.readlines()
  lectura2.close()

  html_Redes = open('redes_sociales.txt','w')
  for line in lineas_htmls:
    fb = patron_FB.match(line)
    #html_Redes.write('  Facebook: ' + fb.group())
    if fb:
      html_Redes.write(fb.group() + '\n')

    twt = patron_TWT.match(line)
    #html_Redes.write('  Twitter: ' + twt.group())
    if twt:
      html_Redes.write(twt.group() + '\n')

    ig = patron_IG.match(line)
    #html_Redes.write('  Instagram: ' + ig.group())
    if ig:
      html_Redes.write(ig.group() + '\n')

  html_Redes.close()

if __name__ == "__main__":
    main_redes()