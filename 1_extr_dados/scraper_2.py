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

    # Essa lista conterá dicionários como elementos, e cada dicionário conterá informações de um produto.
    dados = []

    # Variável auxiliar para garantir que não estaremos pegando URLs de produtos repetidas
    # Não há certeza se os produtos podem aparecer duplicados numa mesma página ou entre as páginas.
    urls_unicas = set()

    # Completando as URLs e iterando sobre as páginas.
    for i in range(1, num_paginas + 1):
        url = f"{url_base}?page={i}"
    
        # Executando um try-except e garantindo que o programa continue mesmo que uma página não possa ser acessada, passando para a próxima.
        page_content = get_page_content(url)
        if page_content is None:
            continue

       # Esse bloco é responsável por acessar os links dos produtos, pegar o código das páginas (de cada produto) e extrair as informações que queremos com a função get_produtc_data
       # Armazena os dicionários retornados por get_product_data em uma lista
        product_links = get_product_links(page_content)
        for product in product_links:
            if product['url'] not in urls_unicas:
                urls_unicas.add(product['url'])
                product_data = get_product_data(product['url'])
                if product_data:
                    dados.append(product_data)
        
        print(f"Dados coletados da página {i}")
        time.sleep(1)  # Pausa para não sobrecarregar o servidor

    # Armazena os dados da lista retornada pelo bloco anterior em um arquivo JSON
    with open('dados_produtos.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

