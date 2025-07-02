from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from uuid import uuid4
import requests
import time


class SvoyDoctorParser:
    BASE_URL = "https://www.svoydoctor.ru/vladeltsam/poleznoe/stati/"
    DOMAIN = "https://www.svoydoctor.ru"

    def __init__(self, max_pages=5):
        self.max_pages = max_pages
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(), options=options)

    def parse(self):
        self.driver.get(self.BASE_URL)
        time.sleep(2)
        articles = []

        for _ in range(self.max_pages):
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            items = soup.select('div.articles-item')

            for item in items:
                title_tag = item.select_one('div.h5 a')
                title = title_tag.text.strip() if title_tag else "Без названия"
                href = title_tag['href'] if title_tag else ""
                source_url = self.DOMAIN + href

                date_tag = item.select_one('p.date')
                published_date = date_tag.text.strip() if date_tag else "Дата неизвестна"

                excerpt_tag = item.select_one('p:not(.date)')
                excerpt = excerpt_tag.text.strip() if excerpt_tag else ""

                img_tag = item.select_one('div.img img')
                img_url = img_tag['src'] if img_tag and img_tag.has_attr('src') else None
                if img_url and img_url.startswith('/'):
                    img_url = self.DOMAIN + img_url

                articles.append({
                    "id": str(uuid4()),
                    "title": title,
                    "excerpt": excerpt,
                    "imageUrl": img_url,
                    "category": "Полезные статьи",
                    "publishedDate": published_date,
                    "sourceUrl": source_url
                })

            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, '.pagination a.active + a')
                self.driver.execute_script("arguments[0].click();", next_button)
                time.sleep(2)
            except:
                print("❌ Следующей страницы нет")
                break

        self.driver.quit()
        return articles


class AmvetParser:
    BASE_URL = "https://amvet.ru"
    PAGE_URL = f"{BASE_URL}/stati-o-boleznyah-zhivotnyh"

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept-Encoding': 'gzip, deflate'
        }

    def parse(self):
        articles = []
        page = 1

        while True:
            url = f"{self.PAGE_URL}/page/{page}/" if page > 1 else self.PAGE_URL + '/'
            print(f"🔄 Парсинг страницы: {url}")

            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print("❌ Страница не найдена, остановка")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.select('article.type-post')
            if not items:
                print("✅ Больше нет статей на странице, остановка")
                break

            for item in items:
                title_tag = item.select_one('h2.entry-title a')
                title = title_tag.text.strip() if title_tag else "Без названия"
                href = title_tag['href'] if title_tag else ""
                source_url = href if href.startswith('http') else self.BASE_URL + href

                date_tag = item.select_one('time.entry-date.published')
                published_date = date_tag.text.strip() if date_tag else "Дата неизвестна"

                excerpt_tag = item.select_one('div.entry-content p')
                excerpt = excerpt_tag.text.strip() if excerpt_tag else ""

                img_tag = item.select_one('.post-thumbnail img')
                img_url = img_tag['src'] if img_tag else None
                if img_url and img_url.startswith('/'):
                    img_url = self.BASE_URL + img_url

                category = "Полезные статьи"
                classes = item.get('class', [])
                if 'category-stati-o-boleznyah-zhivotnyh' in classes:
                    category = "Статьи о болезнях животных"
                elif 'category-o-klinike' in classes:
                    category = "О клинике"
                elif 'category-otzyvy' in classes:
                    category = "Отзывы"

                articles.append({
                    "id": str(uuid4()),
                    "title": title,
                    "excerpt": excerpt,
                    "imageUrl": img_url,
                    "category": category,
                    "publishedDate": published_date,
                    "sourceUrl": source_url
                })

            page += 1

        return articles


class VetAndLifeParser:
    BASE_URL = "https://vetandlife.ru"
    PATH = "/pets/news/"

    def __init__(self, max_pages=1):
        self.max_pages = max_pages
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def parse(self):
        articles = []

        for page in range(1, self.max_pages + 1):
            url = f"{self.BASE_URL}{self.PATH}"
            if page > 1:
                url += f"page/{page}/"

            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print(f"Страница {page} не найдена, остановка.")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.select('div.mini-card')
            if not cards:
                print(f"Нет статей на странице {page}, остановка.")
                break

            for item in cards:
                title_tag = item.select_one('h2.mini-card-title a')
                title = title_tag.text.strip() if title_tag else "Без названия"
                href = title_tag['href'] if title_tag else ""
                source_url = href if href.startswith('http') else self.BASE_URL + href

                date_tag = item.select_one('div.news_date')
                published_date = date_tag.text.strip() if date_tag else "Дата неизвестна"

                img_tag = item.select_one('img.mini-card-img')
                img_url = img_tag['src'] if img_tag else None
                if img_url and img_url.startswith('/'):
                    img_url = self.BASE_URL + img_url

                articles.append({
                    "id": str(uuid4()),
                    "title": title,
                    "excerpt": "",
                    "imageUrl": img_url,
                    "category": "Новости о питомцах",
                    "publishedDate": published_date,
                    "sourceUrl": source_url
                })

        return articles


def parse_all_articles():
    all_articles = []
    all_articles += SvoyDoctorParser().parse()
    all_articles += AmvetParser().parse()
    all_articles += VetAndLifeParser(max_pages=2).parse()
    return all_articles
