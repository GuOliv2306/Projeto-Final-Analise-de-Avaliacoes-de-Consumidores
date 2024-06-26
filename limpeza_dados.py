import json
import string

# Criação da variável pontuação para ficar mais fácil de fazer a remoção delas na lista
pontuacoes = string.punctuation

# Abrindo o arquivo json
with open("dados_produtos_2.json", "r", encoding="utf-8") as file:
    dados = json.load(file)

# Extrair os nomes dos produtos
nomes_produtos = [produto['nome'] for produto in dados]

def condicao_remover(produto):
    # Exemplo: remover produtos cujo nome contém "palavra_especifica" ou cujo preço é inferior a 100
    return produto['avaliacao'] == 'N/A' and produto["depoimentos"] == []

# Remover produtos que atendem à condição
dados = [produto for produto in dados if not condicao_remover(produto)]

# Remover depoimentos vazios dentro de cada produto
for produto in dados:
    produto["depoimentos"] = [depoimento for depoimento in produto["depoimentos"] if depoimento.strip() != ""]

# Salvar os dados atualizados de volta no arquivo JSON
with open('produtos_atualizados_2.json', 'w', encoding='utf-8') as file:
    json.dump(dados, file, ensure_ascii=False, indent=4)