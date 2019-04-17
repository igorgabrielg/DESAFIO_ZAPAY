import unittest
import desafio
from bs4 import BeautifulSoup

code = '<h2 class="woocommerce-loop-product__title">produto1</h2>\
        <span class="price">R$00,00</span>\
        <h2 class="woocommerce-loop-product__title">produto2</h2>\
        <span class="price">R$00,01</span>'


soup = BeautifulSoup(code, 'html.parser')


class MyTest(unittest.TestCase): #Classe de teste do unittest
    def test_gerar_nomes(self): #Teste do Nome
        self.assertEqual('<h2 class="woocommerce-loop-product__title">produto1</h2>', str(desafio.gerar_nomes(soup)[0]))
        self.assertEqual('<h2 class="woocommerce-loop-product__title">produto2</h2>', str(desafio.gerar_nomes(soup)[1]))

    def test_gerar_a_vista(self): #Teste do valor avista
        self.assertEqual('<span class="price">R$00,00</span>', str(desafio.gerar_a_vista(soup)[0]))
        self.assertEqual('<span class="price">R$00,01</span>', str(desafio.gerar_a_vista(soup)[1]))        

if __name__ == '__main__': 
    unittest.main()
