from rest_framework import serializers
from .models import RefAssistant

class RefAssistantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefAssistant
        fields = '__all__'

class RefAssistantRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefAssistant
        fields = '__all__'

class RefAssistantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefAssistant
        fields = '__all__'

class RefAssistantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefAssistant
        fields = '__all__'
