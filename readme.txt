---	DESAFIO ZAPAY	--- 


Instrução: 

Instale as dependências com o comando: 

pip install -r requirements.txt 

Ou 

pipenv install -r requirements.txt 



Implementação: 

1° Passo foi estudar o código da página em busca de padrões: 
- Tags que definiam unicamente os nomes do produto, valores, valores divididos e encontrar a imagem. 

2° Passo foi utilizar o pipenv para criar um ambiente virtual instalando as dependências: 
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

5° Passo foi tratar o dado transformando em informação, ou seja, apenas o texto importante. 

6° Passo foi transformar as informações em um relatorio.csv