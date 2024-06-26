import json
import pandas as pd
from tabela import gerar_tabela

#ler o .json dos produtos
with open('dados_resumidos.json', 'r', encoding='utf-8') as file:
    produtos = json.load(file)


#conversão para data frame pandas
df=pd.DataFrame(produtos)

#data frame para excel
df.to_excel('dados_produtos.xlsx', index=False)
gerar_tabela('dados_produtos.xlsx')






