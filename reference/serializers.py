from rest_framework import serializers
from .models import (
    RefRole, RefProductCategory, RefBreed, RefTypeOfAnimal,
    RefProduct, RefShop
)

# ------------------ РОЛИ ------------------

class RoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefRole
        fields = '__all__'

class RoleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefRole
        fields = '__all__'

class RoleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefRole
        fields = '__all__'

class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefRole
        fields = '__all__'


# -------- КАТЕГОРИИ ПРОДУКЦИЙ ------------

class ProductCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProductCategory
        fields = '__all__'

class ProductCategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProductCategory
        fields = '__all__'

class ProductCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProductCategory
        fields = '__all__'

class ProductCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProductCategory
        fields = '__all__'


# ----------------- ПОРОДЫ -----------------

class BreedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefBreed
        fields = '__all__'

class BreedRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefBreed
        fields = '__all__'

class BreedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefBreed
        fields = '__all__'

class BreedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefBreed
        fields = '__all__'


# ----------- ВИДЫ ЖИВОТНЫХ ---------------

class AnimalTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTypeOfAnimal
        fields = '__all__'

class AnimalTypeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTypeOfAnimal
        fields = '__all__'

class AnimalTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTypeOfAnimal
        fields = '__all__'

class AnimalTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefTypeOfAnimal
        fields = '__all__'


# --------- МЕДИЦИНСКИЕ ПРЕПАРАТЫ ----------

class MedicalProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProduct
        fields = '__all__'

class MedicalProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProduct
        fields = '__all__'

class MedicalProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProduct
        fields = '__all__'

class MedicalProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefProduct
        fields = '__all__'


# --------- ВЕТЕРИНАРНЫЕ АПТЕКИ ------------

class VetPharmacyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefShop
        fields = '__all__'

class VetPharmacyRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefShop
        fields = '__all__'

class VetPharmacyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefShop
        fields = '__all__'

class VetPharmacyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefShop
        fields = '__all__'
