from rest_framework import serializers
from .models import Pet


class PetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields =  "__all__"


class PetRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ("id", )


class PetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ("id", )
