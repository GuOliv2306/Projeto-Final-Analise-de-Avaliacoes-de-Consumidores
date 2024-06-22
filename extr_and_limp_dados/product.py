# product.py
from bs4 import BeautifulSoup
from utils import get_page_content

def get_product_data(url):
    content = get_page_content(url)
    if content is None:
        return None
    soup = BeautifulSoup(content, 'html.parser')
    try:
        # Extrair o nome do produto
        nome = soup.find('h1', class_='ui-pdp-title').get_text(strip=True)
        
        # Extrair e combinar os elementos do preço
        valor = soup.find('span', class_='andes-money-amount__fraction').get_text(strip=True)
        centavos = soup.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-36')
        if centavos:
            centavos = centavos.get_text(strip=True)
            preco = f"{valor},{centavos}"
        else:
            preco = valor
        
        # Extrair a avaliação do produto
        avaliacao_tag = soup.find('span', class_='ui-pdp-review__rating')
        avaliacao = avaliacao_tag.get_text(strip=True) if avaliacao_tag else 'N/A'
        
        # Extrair os depoimentos dos usuários
        depoimentos_tags_1 = soup.find_all('p', class_='ui-review-capability-comments__comment__content')
        depoimentos_tags_2 = soup.find_all('p', class_='ui-review-capability__summary__plain_text__summary_container')
        depoimentos = [depoimento.get_text(strip=True) for depoimento in depoimentos_tags_1 + depoimentos_tags_2]

        return {
            'nome': nome,
            'preco': preco,
            'avaliacao': avaliacao,
            'depoimentos': depoimentos
        }
    except AttributeError as e:
        print(f"Erro ao extrair dados do produto: {e}")
        return None
