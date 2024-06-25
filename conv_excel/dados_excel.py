import json
import pandas as pd
from tabela import gerar_tabela

#ler o .json dos produtos
with open('C:/Users/guguo/PycharmProjects/Projeto-Final-Analise-de-Avaliacoes-de-Consumidores/limp_dados/produtos_atualizados_2.json', 'r', encoding='utf-8') as file:
    produtos = json.load(file)

#retirando as descrições do excel
if isinstance(produtos, list):
    for item in produtos:
        if 'depoimentos' in item:
            del item['depoimentos']
else:
    print("Estrutura do JSON não é uma lista de dicionários.")

#conversão para data frame pandas
df=pd.DataFrame(produtos)

#data frame para excel
df.to_excel('dados_produtos.xlsx', index=False)
gerar_tabela('dados_produtos.xlsx')






