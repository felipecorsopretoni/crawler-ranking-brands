"""
Experimento 01 - Crawler com Scrapy (Ranking The Brands)

Objetivo:
- Deletar tudo no MongoDB e coletar todas as marcas de A a Z.

Como executar:
python -m scrapy runspider experimentos/exp01-crawler-ranking-brands-ab.py
"""
import os
from urllib.parse import parse_qs, urlparse 
import scrapy
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["ranking_brands"]["brands"]

# Deleta tudo antes de começar
db.delete_many({})
print("MongoDB limpo. Iniciando coleta A-Z...")

class RankingBrandsABSpider(scrapy.Spider):
    name = "ranking_brands_ab"
    allowed_domains = ["rankingthebrands.com"]

    start_urls = [
        f"https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter={chr(c)}"
        for c in range(ord("A"), ord("Z") + 1)
    ]

    custom_settings = {
        "ROBOTSTXT_OBEY": True,
        "DOWNLOAD_DELAY": 1.0,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2,
        "LOG_LEVEL": "INFO",
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    }

    def parse(self, response):
        letter = parse_qs(urlparse(response.url).query).get("nameFilter", ["?"])[0]
        brand_links = response.xpath("//a[contains(@href, 'Brand-detail.aspx?brandID=')]")

        self.logger.info(f"Encontradas {len(brand_links)} marcas para letra {letter}")

        for link in brand_links:
            brand_name = link.xpath("normalize-space(.)").get()
            brand_href = link.xpath("@href").get()

            if brand_name and brand_href:
                db.insert_one({
                    "letter": letter,
                    "brand_name": brand_name.strip(),
                    "brand_url": response.urljoin(brand_href),
                    "source_url": response.url,
                })