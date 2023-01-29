import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://ru.sputnik.kg/news"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'User_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36'
}


def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    items = soup.find_all('div', class_="list__item")
    news = []
    for item in items:
        news.append({
            "title": item.find('a', class_='list__title').getText(),
            "link": f"{URL}{item.find('a', class_='list__title').get('href')}",
            "date": datetime.utcfromtimestamp(
                int(item.find('div', class_='list__date').get('data-unixtime'))
            ).strftime('%H:%M:%S %d-%m-%Y')
        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        current_page = get_data(html.text)
        news.extend(current_page)
        return news
    else:
        raise Exception("Error in parser!")


html = get_html(URL)
get_data(html.text)
