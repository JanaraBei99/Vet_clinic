from rest_framework import serializers
from .models import Parsing

class ParsingSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Parsing
        fields = [
            'id',
            'title',
            'excerpt',
            'imageUrl',
            'category',
            'publishedDate',
            'author',
            'sourceUrl'
        ]

    def get_author(self, obj):
        return {
            "name": "Автор не указан",
            "avatarUrl": ""
        }
