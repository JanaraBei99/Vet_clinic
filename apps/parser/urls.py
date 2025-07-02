from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParsingViewSet, ParsedArticlesView, ArticleDataView, ArticleViewsStatsView

router = DefaultRouter()
router.register(r'articles', ParsingViewSet, basename='articles')

urlpatterns = [
    path('article-data/', ArticleDataView.as_view(), name='article_data'),
    path('stats/', ArticleViewsStatsView.as_view(), name='article_views_stats'),
    path('', include(router.urls)),
]
