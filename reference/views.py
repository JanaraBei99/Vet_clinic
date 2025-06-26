from django.shortcuts import render

from rest_framework import viewsets
from .models import RefRole, RefProductCategory, RefBreed, RefTypeOfAnimal, RefProduct, RefShop
from .serializers import (
    RoleSerializer, ProductCategorySerializer, BreedSerializer,
    AnimalSpeciesSerializer, MedicationSerializer, VetStoreSerializer
)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = RefRole.objects.all()
    serializer_class = RoleSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = RefProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = RefBreed.objects.all()
    serializer_class = BreedSerializer

class AnimalSpeciesViewSet(viewsets.ModelViewSet):
    queryset = RefTypeOfAnimal.objects.all()
    serializer_class = AnimalSpeciesSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = RefProduct.objects.all()
    serializer_class = MedicationSerializer

class VetStoreViewSet(viewsets.ModelViewSet):
    queryset = RefShop.objects.all()
    serializer_class = VetStoreSerializer
