# scraper_2.py
import time
import json
from utils_2 import get_page_content, get_product_links
from product_2 import get_product_data
import re

def main():
    # Todas as URLs de sapatênis da versales possuem essa estrutura inicial igual.
    url_base = "https://www.versales.com.br/categoria/masculino-sapatenis/"

    # São ao todo 3 páginas de sapatênis, vamos raspar todas
    num_paginas = 3

    # Essa lista conterá dicionários como elementos, e cada dicionário contém informações de um produto.
    dados = []

    # Variável auxiliar para garantir que não estaremos pegando URLs de produtos repetidas
    # Não há certeza se os produtos podem aparecer duplicados numa mesma página ou entre as páginas.
    urls_unicas = set()

    # Iterando sobre as páginas.
    for i in range(1, num_paginas + 1):
        url = f"{url_base}?page={i}"
    
        # Executando um try-except e garantindo que o programa continue mesmo que uma página não possa ser acessada, passando para a próxima.
        page_content = get_page_content(url)
        if page_content is None:
            continue

        # Recebendo o conteúdo da página e retornando uma lista de dicionários, nos quais cada dicionário armazena o nome de um produto e o link para ele. 
        # Depois iteramos sobre os dicionários da lista e, se o valor da chave url (o link do produto) não estiver no conjunto auxiliar que criamos lá no início, então ele é adicionado a esse conjunto.
        product_links = get_product_links(page_content)
        for product in product_links:
            if product['url'] not in urls_unicas:
                urls_unicas.add(product['url'])
                product_data = get_product_data(product['url'])
                if product_data:
                    dados.append(product_data)
        
        print(f"Dados coletados da página {i}")
        time.sleep(1)  # Pausa para não sobrecarregar o servidor

    # Armazenar os dados em um arquivo JSON
    with open('dados_produtos.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()

