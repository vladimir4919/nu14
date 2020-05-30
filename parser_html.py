import requests
from bs4 import BeautifulSoup
import json
import pprint


domain = 'https://habr.com'
srch = 'ru/hub'
tag = 'java'
url = f'{domain}/{srch}/{tag}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
items = {}

#Первый запрос, парсинг первой страницы и записываем в словарь
result = requests.get(url, headers=headers)
print(result)
soup = BeautifulSoup(result.text, 'html.parser')
pprint.pprint(result.text)
item_tags = soup.find_all('a', class_='post__title_link')#'post__title_link'
pprint.pprint(item_tags)

for item in item_tags[:10]:
    item_link = item.get('href')
    #b.append(item_link)
    item_title = item.get_text()
    items[item_title] = item_link
#print(type(items[item_title]))
#print(href_news)
#pprint.pprint(item_link)

    domain = item_link
    url= f'{domain}'
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_titles_tag = soup.find_all('title')
    print(news_titles_tag)

with open('parse.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False)
