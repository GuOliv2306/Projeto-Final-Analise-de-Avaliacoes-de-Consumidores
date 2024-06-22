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
lista_recorrentes=[]
for palavra, frequencia in mais_comuns:
    lista_recorrentes.append([palavra, frequencia])

categorias_para_adicionar=["suporte", "cadeira", "mesa", "escrivaninha"]

# Função para determinar a categoria com base no preço
def determinar_categoria(nome):
    for each_categotias in categorias_para_adicionar:
        if each_categotias in nome:
            return each_categotias
    return "outros"

# Adicionar o item "categoria" a cada produto
for produto in dados:
    nome_produto=produto["nome"].lower()
    produto['categoria'] = determinar_categoria(nome_produto)

def condicao_remover(produto):
    # Exemplo: remover produtos cujo nome contém "palavra_especifica" ou cujo preço é inferior a 100
    return 'N/A' == produto['avaliacao'] and produto["depoimentos"] == []

# Remover produtos que atendem à condição
dados = [produto for produto in dados if not condicao_remover(produto)]

# Salvar os dados atualizados de volta no arquivo JSON
with open('produtos_atualizados.json', 'w', encoding='utf-8') as file:
    json.dump(dados, file, ensure_ascii=False, indent=4)
