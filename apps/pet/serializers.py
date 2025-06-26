from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


# class PetListSerializer(serializers.ModelSerializer):
#     pass
# class PetRetrieveSerializer(serializers.ModelSerializer):
#     pass
# class PetCreateSerializer(serializers.ModelSerializer):
#     pass
