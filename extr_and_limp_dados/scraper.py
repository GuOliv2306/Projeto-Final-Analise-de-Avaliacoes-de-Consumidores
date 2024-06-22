# scraper.py
import time
import json
from utils import get_page_content, get_product_links
from product import get_product_data

def main():
    url_base = "https://lista.mercadolivre.com.br/casa-moveis-decoracao/moveis-casa/escritorio"
    num_paginas = 42
    dados = []
    urls_unicas = set()

    for i in range(num_paginas):
        if i == 0:
            url = f"{url_base}_NoIndex_True"
        else:
            desde = 49 + 48 * (i - 1)
            url = f"{url_base}_Desde_{desde}_NoIndex_True"
        
        page_content = get_page_content(url)
        if page_content is None:
            continue
        
        product_links = get_product_links(page_content)
        for product in product_links:
            if product['url'] not in urls_unicas:
                urls_unicas.add(product['url'])
                product_data = get_product_data(product['url'])
                if product_data:
                    dados.append(product_data)
        
        print(f"Dados coletados da página {i + 1}")
        time.sleep(1)  # Pausa para não sobrecarregar o servidor

    # Armazenar os dados em um arquivo JSON
    with open('dados_produtos.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
