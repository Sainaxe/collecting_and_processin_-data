import requests
from lxml import html
from pymongo import MongoClient
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
response = requests.get("https://lenta.ru/", headers=headers)
dom = html.fromstring(response.text)
columns = dom.xpath("//div[@class='topnews__column']")
news = []

news.append({
    "Источник": "lenta.ru",
    "Новость": columns[0].xpath(".//h3/text()")[0],
    "Ссылка": columns[0].xpath(".//a[@class='card-big _topnews _news']/@href")[0],
    "Время публикации": columns[0].xpath(".//time[@class='card-big__date']/text()")[0]
})

for col in columns:
    cards = col.xpath(".//a[@class='card-mini _topnews']")
    for card in cards:
        news.append({
            "Источник": "lenta.ru",
            "Новость": card.xpath(".//span/text()")[0],
            "Ссылка": card.xpath("@href")[0],
            "Время публикации": card.xpath(".//time/text()")[0]
        })
client = MongoClient("localhost", 27017)
db = client["News"]
lenta = db.lenta

for elem in news:
    lenta.insert_one(elem)

    list(lenta.find({}))