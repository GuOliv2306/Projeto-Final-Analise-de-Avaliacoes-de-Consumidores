# utils_2.py
import requests
from bs4 import BeautifulSoup

# Essa função é responsável por manter o programa funcionando mesmo que haja algum erro ao tentar abrir uma das páginas.
# Retorna o conteúdo da página ou None
def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Erro de conexão: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de requisição: {e}")
    return None

# Essa função recebe o conteúdo da página web, converte para um objeto BeautifulSoup, encontra os links dos produtos na página e 
# Retorna uma lista de dicionários que possuem informação do nome e URL do produto 
# utils.py

def get_product_links(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    links_produtos = soup.find_all('a', class_='w-100 float-left link-name')
    base_url = "https://www.versales.com.br"  # Defina a URL base

    product_links = []
    for link in links_produtos:
        href = link['href']
        # Verificar se a URL é relativa e, se for, completar com a URL base
        if not href.startswith("http"):
            href = base_url + href
        product_links.append({'nome': link.get_text(strip=True), 'url': href})
    
    return product_links

