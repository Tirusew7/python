from bs4 import BeautifulSoup
import requests
import io
import sys
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bot_token = '6485261689:AAG-L4aPGR6zEW3eOlGNdCJbWW_cL9PRYiI'
chat_id = '529569165'

response = requests.get('https://www.fanabc.com/ስፓርት')
soup = BeautifulSoup(response.text, 'html.parser')
news = soup.find_all('h2', class_='title')
detales = soup.find_all('div', class_='item-conteant')


def send_to_telegram(bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for index, entry in enumerate(news):
    title = entry.get_text(strip=True)
    des = description[index].get_text(strip=True)


    texts = f"news: {title}\ndetales: {des}
    response = send_to_telegram(bot_token, chat_id, texts)
    print(response)
    time.sleep(30)