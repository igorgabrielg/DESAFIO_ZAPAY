import unittest
import desafio
from bs4 import BeautifulSoup

code = '<h2 class="woocommerce-loop-product__title">produto1</h2>\
        <h2 class="woocommerce-loop-product__title">produto2</h2>\
        '

soup = BeautifulSoup(code, 'html.parser')


class MyTest(unittest.TestCase): #Classe de teste do unittest
    def test_gerar_nomes(self): #Metodo de teste do unittest
        self.assertEqual('<h2 class="woocommerce-loop-product__title">produto1</h2>', str(desafio.gerar_nomes(soup)[0]))
        self.assertEqual('<h2 class="woocommerce-loop-product__title">produto2</h2>', str(desafio.gerar_nomes(soup)[1]))


if __name__ == '__main__': 
    unittest.main()
