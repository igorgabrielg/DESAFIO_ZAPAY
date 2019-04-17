# Desafio
import requests
import pandas as pd
from bs4 import BeautifulSoup

nomes = []

# Obtem o codigo
def code_html():
    page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")
    return BeautifulSoup(page.text, 'html.parser')

# Obtem os nomes
def gerar_nomes(soup):
    return soup.findAll("h2", {"class": "woocommerce-loop-product__title"})

# Gera o relatorio
def gerar_relatorio(codnomes):
    for i in (codnomes):
        # Nome
        nomes.append(i.text)

    date = {
            'Nomes': nomes,
        }
    print(date)

    return pd.DataFrame(date)

def run():
    soup = code_html()
    codnomes = gerar_nomes(soup)
    df = gerar_relatorio(codnomes)
    
    print(df)

if __name__ == '__main__':
    run()
