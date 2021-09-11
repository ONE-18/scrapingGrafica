from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.es/s?k=tarjetas+gráficas+3060&s=price-asc-rank&dc&adgrpid=109724649253&gclid=CjwKCAjwhOyJBhA4EiwAEcJdcXXieJuLuKt73VXoPnh2fMJh1EgCMfaAQ7d3RmawOuivq-GP89nC3RoCdmYQAvD_BwE&hvadid=468711882938&hvdev=c&hvlocphy=1005508&hvnetw=g&hvqmt=e&hvrand=9180893437774154674&hvtargid=kwd-1055595723489&hydadcr=13811_1743264&qid=1631313285&tag=hydes-21&ref=sr_st_price-asc-rank'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Precios
raw = soup.find_all('span', class_='a-offscreen')

precios = list()

for i in raw:
    precios.append(i.text)

for precio in precios:
    print(precio)

print(len(precios))

# Nombres
raw = soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')

nombres = list()

for i in raw:
    nombres.append(i.text)

for nombre in nombres:
    print(nombre)

print(len(nombres))

'''for element in soup.find_all("tag"):
    for a in element.find_all("a"):
        print(a['data-price'])'''

'''
horasRaw = soup.find_all('div', class_='col-xs-9')

hora = list()

for i in horasRaw:
    hora.append(i.text.split(': '))
'''
