import openai
import json

# Substitua pela sua chave de API
openai.api_key = 'minha-chave'

def analisar_sentimento(texto):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": f"Analise o sentimento do seguinte texto: {texto}"}
        ],
        max_tokens=60
    )
    return response.choices[0].message['content'].strip()

def processar_produto(produto):
    insights = []
    for depoimento in produto.get('depoimentos', []):
        sentimento = analisar_sentimento(depoimento)
        insights.append({
            'depoimento': depoimento,
            'sentimento': sentimento
        })
    return insights

# Carregar o arquivo JSON e processar os produtos
with open('rodutos_atualizados_2.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)

for produto in produtos:
    produto['insights'] = processar_produto(produto)

# Salvar os produtos atualizados com os insights
with open('produtos_com_insights.json', 'w', encoding='utf-8') as f:
    json.dump(produtos, f, ensure_ascii=False, indent=4)
