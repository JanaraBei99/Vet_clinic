from rest_framework import serializers
from .models import Pet

class PetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'breed', 'date_of_birth', 'weight', 'avatar_url']

class PetRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'species', 'breed', 'date_of_birth', 'weight', 'avatar_url']

class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'date_of_birth', 'weight', 'avatar_url']

class PetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'date_of_birth', 'weight', 'avatar_url']



# class PetListSerializer(serializers.ModelSerializer):
#     pass
# class PetRetrieveSerializer(serializers.ModelSerializer):
#     pass
# class PetCreateSerializer(serializers.ModelSerializer):
#     pass
