# utils.py
import requests
from bs4 import BeautifulSoup

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

def get_product_links(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    links_produtos = soup.find_all('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')
    return [{'nome': link.get_text(strip=True), 'url': link['href']} for link in links_produtos]
