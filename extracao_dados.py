from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://lista.mercadolivre.com.br/escritorio#deal_print_id=aa12b6d0-2a78-11ef-8e4e-537da5717dc2&c_id=special-withoutlabel&c_element_order=2&c_campaign=ESPECIAL_X3_ESCRITORIO&c_uid=aa12b6d0-2a78-11ef-8e4e-537da5717dc2'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

cells = soup.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated')

products = []
avaliations = []
descriptions = []

for i in range(len(cells)):
    product = cells[i].find('a').text.strip()
    avaliation = cells[i].find('span', class_='ui-search-reviews_rating-numer')
    products.append(product)
    avaliations.append(avaliation)


data = {'Product': products,
        'Avaliation': avaliations}
df = pd.DataFrame(data)
print(df)

