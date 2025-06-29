from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from uuid import uuid4
import requests

def scrape_article_details():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Без интерфейса
    driver = webdriver.Chrome(service=Service(), options=options)

    BASE_URL = "https://www.svoydoctor.ru/vladeltsam/poleznoe/stati/"
    driver.get(BASE_URL)
    time.sleep(2)

    articles = []

    for _ in range(5):  # Например, 5 страниц максимум
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.select('div.articles-item')

        for item in items:
            title_tag = item.select_one('div.h5 a')
            title = title_tag.text.strip() if title_tag else "Без названия"
            href = title_tag['href'] if title_tag else ""
            source_url = "https://www.svoydoctor.ru" + href

            date_tag = item.select_one('p.date')
            published_date = date_tag.text.strip() if date_tag else "Дата неизвестна"

            excerpt_tag = item.select_one('p:not(.date)')
            excerpt = excerpt_tag.text.strip() if excerpt_tag else ""

            img_tag = item.select_one('div.img img')
            img_url = img_tag['src'] if img_tag and img_tag.has_attr('src') else None
            if img_url and img_url.startswith('/'):
                img_url = "https://www.svoydoctor.ru" + img_url

            article_data = {
                "id": str(uuid4()),
                "title": title,
                "excerpt": excerpt,
                "imageUrl": img_url,
                "category": "Полезные статьи",
                "publishedDate": published_date,
                "sourceUrl": source_url
            }

            articles.append(article_data)

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.pagination a.active + a')
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(2)
        except:
            print("❌ Следующей страницы нет")
            break

    driver.quit()
    return articles


def second_parsing():
    BASE_URL = "https://amvet.ru"
    PAGE_URL = f"{BASE_URL}/stati-o-boleznyah-zhivotnyh"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding': 'gzip, deflate'
    }

    articles = []
    page = 1

    while True:
        url = f"{PAGE_URL}/page/{page}/" if page > 1 else PAGE_URL + '/'
        print(f"🔄 Парсинг страницы: {url}")

        response = requests.get(url, headers=headers)
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
            source_url = href if href.startswith('http') else BASE_URL + href

            date_tag = item.select_one('time.entry-date.published')
            published_date = date_tag.text.strip() if date_tag else "Дата неизвестна"

            excerpt_tag = item.select_one('div.entry-content p')
            excerpt = excerpt_tag.text.strip() if excerpt_tag else ""

            img_tag = item.select_one('.post-thumbnail img')
            img_url = img_tag['src'] if img_tag else None
            if img_url and img_url.startswith('/'):
                img_url = BASE_URL + img_url

            category = "Полезные статьи"
            if 'category-stati-o-boleznyah-zhivotnyh' in item.get('class', []):
                category = "Статьи о болезнях животных"
            elif 'category-o-klinike' in item.get('class', []):
                category = "О клинике"
            elif 'category-otzyvy' in item.get('class', []):
                category = "Отзывы"

            article_data = {
                "id": str(uuid4()),
                "title": title,
                "excerpt": excerpt,
                "imageUrl": img_url,
                "category": category,
                "publishedDate": published_date,
                "sourceUrl": source_url
            }

            articles.append(article_data)

        page += 1

    return articles


def third_parsing(max_pages=1):
    BASE_URL = "https://vetandlife.ru"
    base_path = "/pets/news/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    articles = []

    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}{base_path}"
        if page > 1:
            url += f"page/{page}/"

        response = requests.get(url, headers=headers)
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
            source_url = href if href.startswith('http') else BASE_URL + href

            date_tag = item.select_one('div.news_date')
            published_date = date_tag.text.strip() if date_tag else "Дата неизвестна"

            img_tag = item.select_one('img.mini-card-img')
            img_url = img_tag['src'] if img_tag else None
            if img_url and img_url.startswith('/'):
                img_url = BASE_URL + img_url

            article_data = {
                "id": str(uuid4()),
                "title": title,
                "excerpt": "",
                "imageUrl": img_url,
                "category": "Новости о питомцах",
                "publishedDate": published_date,
                "sourceUrl": source_url
            }

            articles.append(article_data)

    return articles


def parse_all_articles():
    return scrape_article_details() + second_parsing() + third_parsing()