from django.http import JsonResponse
from .scraper import parse_all_articles
from .models import ArticleView
from .utils import get_client_ip
from django.db import models

def get_article_data(request):
    articles = parse_all_articles()
    if not isinstance(articles, list):
        articles = [articles]

    ip = get_client_ip(request)

    for article in articles:
        source_url = article.get("sourceUrl")
        if source_url is None:
            print("Article skipped: missing sourceUrl")
            continue

        if not ArticleView.objects.filter(sourceUrl=source_url).exists():
            try:
                ArticleView.objects.create(
                    title=article.get("title", "No title"),
                    excerpt=article.get("excerpt", ""),
                    imageUrl=article.get("imageUrl", None),
                    category=article.get("category", None),
                    publishedDate=article.get("publishedDate", ""),
                    sourceUrl=source_url,
                    ip_address=ip,
                )
            except Exception as e:
                print(f"Error saving article with sourceUrl={source_url}: {e}")

    return JsonResponse(articles, safe=False)


def article_views_stats(request):
    stats = ArticleView.objects.values('article_url').annotate(
        count=models.Count('id')
    )
    return JsonResponse(list(stats), safe=False)


