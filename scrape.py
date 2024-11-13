import requests
from bs4 import BeautifulSoup
import json

url = 'https://example-news-website.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data (titles, summaries, etc.)
news_items = []
for item in soup.find_all('div', class_='news-item'):
    title = item.find('h2').text
    summary = item.find('p').text
    news_items.append({'title': title, 'summary': summary})

# Save scraped data to a JSON file (or post directly)
with open('news_data.json', 'w') as f:
    json.dump(news_items, f)
