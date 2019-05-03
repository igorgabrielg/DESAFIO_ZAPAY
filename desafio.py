import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

nomes = []
links = []
avistas = []
divididos = []

# Obtem codigo da pagina

try:
    page = requests.get("https://nerdstore.com.br/categoria/especiais/game-of-thrones/")
    soup = BeautifulSoup(page.text, 'html.parser')
except OSError:
    print("Verifique sua conexão com a internet e tente novamente.")


# Decorador
def obter_dados(soup, tag, tipo):
    # Função Interna
    def valida(func):
        def inner(*args):
                return soup.findAll(tag, {"class": tipo})
        return inner
    return valida


# Obtem tag dos nomes
@obter_dados(soup, "h2", "woocommerce-loop-product__title")
def gerar_nomes():
    return valor


# Obtem tag dos valores a vista
@obter_dados(soup, "span", "price")
def gerar_a_vista():
    return valor


# Obtem tag dos valor dividido
@obter_dados(soup, "div", "installments")
def gerar_dividido():
    return valor


# Obtem tag dos link das imagens
@obter_dados(soup, "li", re.compile("product type-product"))
def gerar_link():
    return valor


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

    df.to_csv('relatorio_dos_produtos.csv')

    return df


def run():

    codnomes = gerar_nomes()
    codimgs = gerar_link()
    codavistas = gerar_a_vista()
    codivididos = gerar_dividido()
    print(gerar_relatorio(codnomes, codimgs, codavistas, codivididos))


if __name__ == '__main__':
    run()
