# product_2.py
from bs4 import BeautifulSoup
from utils_2 import get_page_content
import re

def get_product_data(url):
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
        depoimentos_tags_head = [tag.get_text(strip=True) for tag in soup.find_all('p', class_='product-rating__review-list__title')]
        depoimentos_tags_nome = [tag.get_text(strip=True) for tag in soup.find_all('p', class_='product-rating__detail__name')]
        depoimentos_tags_msg = [tag.get_text(strip=True) for tag in soup.find_all('p', class_='product-rating__detail__message')]
        depoimentos = [f"{a} - {b} - {c}" for a, b, c in zip(depoimentos_tags_head, depoimentos_tags_nome, depoimentos_tags_msg)]

        return {
            'nome': nome,
            'preco': preco,
            'avaliacao': avaliacao,
            'quantidade-de-avaliacoes': qAva,
            'depoimentos': depoimentos
        }
    except AttributeError as e:
        print(f"Erro ao extrair dados do produto: {e}")
        return None


