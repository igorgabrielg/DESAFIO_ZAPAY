import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

nomes = []
links = []
avistas = []
divididos = []


# Obtem codigo da pagina
def code_html():
    page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")
    return BeautifulSoup(page.text, 'html.parser')


# Obtem tag dos nomes
def gerar_nomes(soup):
    return soup.findAll("h2", {"class": "woocommerce-loop-product__title"})


# Obtem tag dos valores a vista
def gerar_a_vista(soup):
    return soup.findAll("span", {"class": "price"})


# Obtem tag dos valor dividido
def gerar_dividido(soup):
    return soup.findAll("div", {"class": "installments"})


# Obtem tag dos link das imagens
def gerar_link(soup):
    return soup.findAll("li", attrs={'class': re.compile("type-product status-publish")})


# Gera Relatorio apenas os
def gerar_relatorio(codnomes, codimgs, codavistas, codivididos):
    for i in range(len(codnomes)):
        # Nome
        nomes.append(codnomes[i].text)
        # Link
        links.append(codimgs[i].img.get('src'))
        # Valores a vista
        avistas.append(codavistas[i].text)
        # Dividido
        divididos.append(codivididos[i].text)

    date = {
        'Nomes': nomes,
        'Links': links,
        'Valores a vista': avistas,
        'Valores dividido': divididos
        }

    df = pd.DataFrame(date)

    return df


def run():
    soup = code_html()
    codnomes = gerar_nomes(soup)
    codimgs = gerar_link(soup)
    codavistas = gerar_a_vista(soup)
    codivididos = gerar_dividido(soup)
    print(gerar_relatorio(codnomes, codimgs, codavistas, codivididos))


if __name__ == '__main__':
    run()
