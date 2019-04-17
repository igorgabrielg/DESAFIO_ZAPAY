# Desafio
import requests
import pandas as pd
from bs4 import BeautifulSoup

nomes = []
avistas = []

# Obtem o codigo
def code_html():
    page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")
    return BeautifulSoup(page.text, 'html.parser')

# Obtem os nomes
def gerar_nomes(soup):
    return soup.findAll("h2", {"class": "woocommerce-loop-product__title"})

def gerar_a_vista(soup):
    return soup.findAll("span", {"class": "price"})

# Gera o relatorio dos
def gerar_relatorio(codnomes, codavistas):
    for i in range(len(codnomes)):
        # Nome
        nomes.append(codnomes[i].text)
        # valor a vista
        avistas.append(codavistas[i].text)

    date = {
            'Nomes': nomes,
            'Valores a vista': avistas
        }

    df = pd.DataFrame(date)

    return df

def run():
    soup = code_html()
    codnomes = gerar_nomes(soup)
    codavistas = gerar_a_vista(soup)
    print(gerar_relatorio(codnomes, codavistas))

if __name__ == '__main__':
    run()
