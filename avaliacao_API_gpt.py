import json
import openai
import re

# Configuração da API diretamente no código
openai.api_key = ''  # Substitua pela sua chave real


# Função para extrair a data, autor e texto do depoimento
def extrair_dados_depoimento(depoimento):
    match = re.match(r"(.) - ([^-]+) - (.)", depoimento)
    if match:
        return match.group(3), match.group(2), match.group(1)
    return depoimento, "", ""


# Função para gerar resumo usando a nova interface ChatCompletion
def gerar_resumo(texto):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ou "gpt-4", dependendo da sua conta e acesso
            messages=[
                {"role": "system", "content": "Você é um assistente que classifica depoimentos de clientes com base em 3 aspectos: positivo, negativo ou neutro."},
                {"role": "user", "content": f"Classifique o seguinte depoimento: {texto}"}
            ],
            max_tokens=60
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Erro ao resumir o texto: {e}")
        return "Erro ao gerar resumo"


# Função para carregar JSON
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []


# Função para salvar JSON
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


# Nome do arquivo original e arquivo de saída
nome_arquivo_original = 'produtos_atualizados_2.json'
nome_arquivo_saida = 'dados_avaliados.json'

# Carregar o JSON
dados = carregar_dados(nome_arquivo_original)

# Aplicar resumo e substituir depoimentos originais, salvando progressivamente
if dados:
    for item in dados:
        if 'depoimentos' in item:
            for i, depoimento in enumerate(item['depoimentos']):
                print(f"Processando depoimento {i + 1}/{len(item['depoimentos'])}")

                # Extrair dados do depoimento
                texto, autor, data = extrair_dados_depoimento(depoimento)

                # Gerar e substituir o resumo
                resumo = gerar_resumo(texto)
                print(f"Resumo gerado: {resumo}")

                # Recompôr o depoimento com o resumo
                if autor and data:
                    item['depoimentos'][i] = f"{resumo} - {autor} - {data}"
                else:
                    item['depoimentos'][i] = resumo

                # Salvar os dados com o resumo atualizado
                salvar_dados(nome_arquivo_saida, dados)
    print("Processamento completo.")
else:
    print("Nenhum dado foi processado devido a erro ao carregar o JSON.")