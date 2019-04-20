Instrução:

Instale as dependencias com:

pip install -r requirements.txt


DESAFIO ZAPAY

1° Passo foi estudar o codigo da pagina em busca de padrões:
- Tags que definiam unicamente os nomes do produto, valores, valores dividido e encontrar a imagem.

2° Passo foi utilizar o pipenv para criar um ambiente virtual instalando as dependencias:
- re
- requests
- pandas
- bs4

3° Passo foi obter o codigo html utilizando request

4° Passo foi usar a biblioteca bs4 para buscar as tags que definem cada um dos dados.
- Tag do nome do produto
- Tag do valor a vista
- Tag do valor dividido
- Tag do link da imagem

5° Passo foi tratar o dado trasformando em informação, ou seja, apenas o texto importante.

6° Passo foi trasformar as informações em um relatorio CSV.