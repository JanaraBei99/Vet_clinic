from .models import (
    RefRole,
    RefProductCategory,
    RefBreed,
    RefTypeOfAnimal,
    RefProduct,
    RefShop,
)
from rest_framework import serializers


class RefRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefRole
        fields = '__all__'


class RefProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProductCategory
        fields = '__all__'


class RefBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefBreed
        fields = '__all__'


class RefShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefShop
        fields = '__all__'


class RefTypeOfAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTypeOfAnimal
        fields = '__all__'


class RefProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProduct
        fields = '__all__'

