# product_2.py
from bs4 import BeautifulSoup
from utils_2 import get_page_content
import re

def get_product_data(url):

    """
Extrai informações detalhadas de um produto de uma página web especificada por uma URL.

Parâmetros:
url (str): A URL da página do produto de onde as informações serão extraídas.

Retorna:
dict: Um dicionário contendo informações sobre o produto, incluindo nome, preço, avaliação média, quantidade de avaliações e depoimentos de usuários.
Retorna None se a extração falhar ou se o conteúdo da página não puder ser obtido.

O dicionário retornado tem a seguinte estrutura:
    {
        'nome': str,                  # O nome do produto.
        'preco': str,                 # O preço do produto.
        'avaliacao': str,             # A avaliação média do produto.
        'quantidade-de-avaliacoes': str, # A quantidade de avaliações do produto.
        'depoimentos': list           # Lista de strings contendo depoimentos dos usuários.
    }

Exceções:
AttributeError: Levantada se algum dos elementos necessários não for encontrado na página.

Detalhes:
- A função primeiramente tenta obter o conteúdo da página. Se falhar, retorna None.
- Usa BeautifulSoup para fazer parsing do HTML.
- Extrai o nome, preço, avaliações e depoimentos do produto usando seletores específicos.
- Trata exceções para garantir que qualquer falha na extração não interrompa a execução do programa.
    """

    content = get_page_content(url)
    if content is None:
        return None
    soup = BeautifulSoup(content, 'html.parser')
    try:
        # Extrair o nome do produto
        nome = soup.find('span', id=re.compile('js-product_name__product_detail_')).get_text(strip=True)
        
        # Extrair o elemento do preço
        preco = soup.find('b', class_='cost').get_text(strip=True)[3:8]
        
        # Extrair a avaliação do produto
        avaliacao_tag = soup.find('span', class_='product-rating__stars__count')
        if "0,0" not in avaliacao_tag.get_text(strip=True):
            avaliacao = avaliacao_tag.get_text(strip=True)[0:3]
            qAva = avaliacao_tag.get_text(strip=True)[19:21]
        else:
            avaliacao = "N/A"
            qAva = "0"
        
        # Extrair os depoimentos dos usuários
        depoimentos_tags_msg = [tag.get_text(strip=True) for tag in soup.find_all('p', class_='product-rating__detail__message')]

        return {
            'nome': nome,
            'preco': preco,
            'avaliacao': avaliacao,
            'quantidade-de-avaliacoes': qAva,
            'depoimentos': depoimentos_tags_msg
        }
    except AttributeError as e:
        print(f"Erro ao extrair dados do produto: {e}")
        return None



