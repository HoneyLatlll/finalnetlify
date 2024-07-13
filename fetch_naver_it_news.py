import requests
from bs4 import BeautifulSoup
import json

def fetch_naver_it_news():
    url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=105'  # 네이버 IT 뉴스 URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_items = []
    
    # 네이버 IT 뉴스 페이지의 헤드라인을 크롤링 (적절한 CSS 선택자 사용)
    headlines = soup.select('ul.type06_headline li dl dt:not(.photo) a')
    for headline in headlines:
        title = headline.text.strip()
        link = headline['href']
        news_items.append({'title': title, 'link': link})
    
    return news_items

def save_news_to_json(news):
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news = fetch_naver_it_news()
    save_news_to_json(news)
