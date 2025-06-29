from django.http import JsonResponse
from django.db import models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Parsing
from .serializers import ParsingSerializer
from .scraper import parse_all_articles
from .utils import get_client_ip

class ArticleDataView(APIView):
    def get(self, request, *args, **kwargs):
        articles = parse_all_articles()
        if not isinstance(articles, list):
            articles = [articles]

        ip = get_client_ip(request)

        created_articles = []
        errors = []

        for article in articles:
            source_url = article.get("sourceUrl")
            if not source_url:
                # Можно логировать или пропустить
                continue

            if not Parsing.objects.filter(sourceUrl=source_url).exists():
                try:
                    obj = Parsing.objects.create(
                        title=article.get("title", "No title"),
                        excerpt=article.get("excerpt", ""),
                        imageUrl=article.get("image_url", None),  # исправил image_rl -> imageUrl
                        category=article.get("category", None),
                        publishedDate=article.get("published_date", ""),
                        sourceUrl=source_url,
                        ip_address=ip,
                    )
                    created_articles.append(obj)
                except Exception as e:
                    errors.append(f"Error saving article {source_url}: {e}")

        serializer = ParsingSerializer(created_articles, many=True)
        return Response({
            "created": serializer.data,
            "errors": errors
        }, status=status.HTTP_201_CREATED if created_articles else status.HTTP_200_OK)

class ArticleViewsStatsView(APIView):
    def get(self, request, *args, **kwargs):
        stats = Parsing.objects.values('sourceUrl').annotate(
            count=Count('id')
        )
        return Response(stats)

class ParsedArticlesView(APIView):
    def get(self, request):
        articles = Parsing.objects.all()
        serializer = ParsingSerializer(articles, many=True)
        return Response(serializer.data)

class ParsingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Parsing.objects.all()
    serializer_class = ParsingSerializer
