from rest_framework import serializers
from .models import RefRole, RefProductCategory, RefBreed, RefTypeOfAnimal, RefProduct, RefShop

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefRole
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProductCategory
        fields = '__all__'

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefBreed
        fields = '__all__'

class AnimalSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTypeOfAnimal
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProduct
        fields = '__all__'

class VetStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefShop
        fields = '__all__'