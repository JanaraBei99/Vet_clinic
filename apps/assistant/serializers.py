from rest_framework import serializers
from .models import Assistant


class AssistantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'


class AssistantRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'


class AssistantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'


class AssistantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
