import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

# Step 1: ニュースページへアクセス
url = "https://news.yahoo.co.jp"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: ニュースリンクを抽出
links = soup.find_all('a', href=lambda x: x and '/pickup/' in x)

# Step 3: 重複除去＆上位10件抽出
titles = []
seen = set()
for link in links:
    title = link.text.strip()
    if title and title not in seen:
        titles.append(title)
        seen.add(title)
    if len(titles) >= 10:
        break

# Step 4: CSVフォルダとファイル名の設定
os.makedirs('output', exist_ok=True)  # outputフォルダを作成（すでにあればスキップ）
date_str = datetime.now().strftime('%Y-%m-%d')
filename = f'output/news_{date_str}.csv'

# CSV出力
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['No', 'Title'])
    for i, title in enumerate(titles, start=1):
        writer.writerow([i, title])

print(f"ニュースタイトルを {filename} に保存しました。")