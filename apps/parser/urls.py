from django.urls import path
from .views import get_article_data, article_views_stats, parse_all_articles

urlpatterns = [
    path('article-data/', get_article_data, name='article_data'),
    path('stats/', article_views_stats, name='article_views_stats'),
    path('api/parse-articles/', parse_all_articles, name='parse_all_articles'),
]
