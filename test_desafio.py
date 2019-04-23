import os
import unittest
import desafio
from bs4 import BeautifulSoup


# classe basica do tdd
class MyTest(unittest.TestCase):

    # Configura
    def setUp(self):
        self.code = '<li class="type-product status-publish"><img src="link1.html"></img></li>\
        <h2 class="woocommerce-loop-product__title">produto1</h2>\
        <span class="price">R$00,00</span>\
        <div class="installments">div 1</div>\
        <li class="type-product status-publish"><img src="link2.html"></img></li>\
        <h2 class="woocommerce-loop-product__title">produto2</h2>\
        <span class="price">R$00,01</span>\
       <div class="installments">div 2</div>'
        
        self.soup = BeautifulSoup(self.code, 'html.parser')
        self.codnomes = desafio.gerar_nomes(self.soup)
        self.codimgs = desafio.gerar_link(self.soup)
        self.codavistas = desafio.gerar_a_vista(self.soup)
        self.codivididos = desafio.gerar_dividido(self.soup)

    # Desmonta
    def teardown(self):
        del self.code
        del self.soup
        del self.codnomes
        del self.codimgs
        del self.codavistas
        del self.codivididos

    # Teste Obter Codigo HTML
    def test_code_html(self):
        soup = desafio.code_html()
        self.assertEqual("Game of Thrones na Nerdstore", soup.title.text)

    # Teste Nomes
    def test_gerar_nomes(self):
        self.assertEqual('<h2 class="woocommerce-loop-product__title">produto1</h2>', str(self.codnomes[0]))
        self.assertEqual('<h2 class="woocommerce-loop-product__title">produto2</h2>', str(self.codnomes[1]))

    # Teste links
    def test_gerar_link(self):
        self.assertEqual('<li class="type-product status-publish"><img src="link1.html"/></li>', str(self.codimgs[0]))
        self.assertEqual('<li class="type-product status-publish"><img src="link2.html"/></li>', str(self.codimgs[1]))

    # Teste a vista
    def test_gerar_a_vista(self):
        self.assertEqual('<span class="price">R$00,00</span>', str(self.codavistas[0]))
        self.assertEqual('<span class="price">R$00,01</span>', str(self.codavistas[1]))

    # Teste dividido
    def test_gerar_dividido(self):
        self.assertEqual('<div class="installments">div 1</div>', str(self.codivididos[0]))
        self.assertEqual('<div class="installments">div 2</div>', str(self.codivididos[1]))

    # Teste relatorio
    def test_gerar_relatorio(self):
        codnomes = desafio.gerar_nomes(self.soup)
        codimgs = desafio.gerar_link(self.soup)
        codavistas = desafio.gerar_a_vista(self.soup)
        codivididos = desafio.gerar_dividido(self.soup)

        self.assertEqual({'Links': {0: 'link1.html', 1: 'link2.html'},
                          'Nomes': {0: 'produto1', 1: 'produto2'},
                          'Valores a vista': {0: 'R$00,00', 1: 'R$00,01'},
                          'Valores dividido': {0: 'div 1', 1: 'div 2'}},
                         desafio.gerar_relatorio(codnomes, codimgs, codavistas, codivididos).to_dict())
        
        self.assertTrue(os.path.isfile(os.path.join(os.path.abspath(''), 'relatorio_dos_produtos.csv')))
        


if __name__ == '__main__': 
    unittest.main()
