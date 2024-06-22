import json 
import string
from collections import Counter

#Criação da variável pontuação para ficar mais fácil de fazer a remoção delas na lista
pontuacoes=string.punctuation

#Abrindo o arquivo json
with open("dados_produtos.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

# Extrair os nomes dos produtos
nomes_produtos = [produto['nome'] for produto in dados]

#Criação de uma matriz que contem listas com as palavras de cada nome dos produtos
matriz_com_palavras=[]
for i in range (len(dados)):
    for char in nomes_produtos[i].split():
        if char in pontuacoes:
            nomes_produtos[i] = nomes_produtos[i].replace(char, "")
    matriz_com_palavras.append(nomes_produtos[i].split())

#Transformando a matriz em uma única lista
todas_palavras = [palavra for sublista in matriz_com_palavras for palavra in sublista]

# Contar a frequência das palavras
contador = Counter(todas_palavras)

# Identificar as 10 palavras mais recorrentes
mais_comuns = contador.most_common(20)

# Exibir os resultados
for palavra, frequencia in mais_comuns:
    print(f'Palavra: {palavra}, Frequência: {frequencia}')