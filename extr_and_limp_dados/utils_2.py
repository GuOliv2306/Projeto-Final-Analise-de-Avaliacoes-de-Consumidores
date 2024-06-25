# utils_2.py
import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    """
Realiza uma solicitação GET para a URL fornecida e retorna o conteúdo da página.

Parâmetros:
url (str): A URL da página web a ser acessada.

Retorna:
bytes: O conteúdo da página em bytes se a solicitação for bem-sucedida.
None: Retorna None se ocorrer algum erro durante a solicitação.

Exceções:
Prints mensagens de erro específicas para cada tipo de exceção capturada (HTTPError, ConnectionError, RequestException).

    """
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

    """
Extrai links de produtos de uma página web dada, completando URLs relativas com a URL base.

Parâmetros:
page_content (bytes): O conteúdo da página em bytes, no qual a busca por links será realizada.

Retorna:
list: Uma lista de dicionários, cada dicionário contendo 'nome' e 'url' do produto.
'nome' é o texto do link do produto e 'url' é o link absoluto do produto.

Detalhes:
- Utiliza BeautifulSoup para fazer parsing do HTML.
- Busca por elementos de link com uma classe CSS específica ('w-100 float-left link-name').
- Checa se o link é relativo e, se for, prepende a URL base antes de adicioná-lo à lista de retorno.
    
    """
    soup = BeautifulSoup(page_content, 'html.parser')
    links_produtos = soup.find_all('a', class_='w-100 float-left link-name')
    base_url = "https://www.versales.com.br"

    product_links = []
    for link in links_produtos:
        href = link['href']
        # Verificar se a URL é relativa e, se for, completar com a URL base
        if not href.startswith("http"):
            href = base_url + href
        product_links.append({'nome': link.get_text(strip=True), 'url': href})
    
    return product_links

