import requests
from bs4 import BeautifulSoup
import json

def fetch_naver_it_news():
    url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=105'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve news, status code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = []
    
    # CSS 선택자를 사용하여 헤드라인 선택
    headlines = soup.select('ul.type06_headline li dl dt:not(.photo) a')
    
    if not headlines:
        print("No headlines found. Please check the CSS selector or the HTML structure.")
    
    for headline in headlines[:5]:
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
    print("News saved to news.json")
