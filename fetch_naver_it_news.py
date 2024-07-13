import requests
from bs4 import BeautifulSoup
import json

def fetch_naver_it_news():
    url = 'https://newsstand.naver.com/?list=ct4'  # 네이버 IT 뉴스 URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_items = []
    
    # 네이버 뉴스스탠드의 IT 뉴스 항목을 크롤링 (적절한 CSS 선택자 사용)
    articles = soup.select('div._4F2Kn article')
    for article in articles:
        title = article.select_one('strong').text
        link = article.select_one('a')['href']
        image_url = article.select_one('img')['src']
        news_items.append({'title': title, 'link': link, 'image_url': image_url})
    
    return news_items

def save_news_to_json(news):
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news = fetch_naver_it_news()
    save_news_to_json(news)
