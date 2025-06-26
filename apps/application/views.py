from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (
    RefRole, RefProductCategory, RefBreed, RefTypeOfAnimal,
    RefProduct, RefShop
)
from .serializers import (
    RoleListSerializer, RoleRetrieveSerializer, RoleCreateSerializer, RoleUpdateSerializer,
    ProductCategoryListSerializer, ProductCategoryRetrieveSerializer, ProductCategoryCreateSerializer, ProductCategoryUpdateSerializer,
    BreedListSerializer, BreedRetrieveSerializer, BreedCreateSerializer, BreedUpdateSerializer,
    AnimalTypeListSerializer, AnimalTypeRetrieveSerializer, AnimalTypeCreateSerializer, AnimalTypeUpdateSerializer,
    MedicalProductListSerializer, MedicalProductRetrieveSerializer, MedicalProductCreateSerializer, MedicalProductUpdateSerializer,
    VetPharmacyListSerializer, VetPharmacyRetrieveSerializer, VetPharmacyCreateSerializer, VetPharmacyUpdateSerializer
)

# ---------------- РОЛИ ------------------

class RoleViewSet(viewsets.ModelViewSet):
    queryset = RefRole.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RoleListSerializer
        elif self.action == 'retrieve':
            return RoleRetrieveSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return RoleCreateSerializer if self.action == 'create' else RoleUpdateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- КАТЕГОРИИ ПРОДУКЦИЙ -----------

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = RefProductCategory.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductCategoryListSerializer
        elif self.action == 'retrieve':
            return ProductCategoryRetrieveSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ProductCategoryCreateSerializer if self.action == 'create' else ProductCategoryUpdateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------- ПОРОДЫ ------------------

class BreedViewSet(viewsets.ModelViewSet):
    queryset = RefBreed.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BreedListSerializer
        elif self.action == 'retrieve':
            return BreedRetrieveSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return BreedCreateSerializer if self.action == 'create' else BreedUpdateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------- ВИДЫ ЖИВОТНЫХ ------------------

class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = RefTypeOfAnimal.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AnimalTypeListSerializer
        elif self.action == 'retrieve':
            return AnimalTypeRetrieveSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return AnimalTypeCreateSerializer if self.action == 'create' else AnimalTypeUpdateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------- МЕДИЦИНСКИЕ ПРЕПАРАТЫ ----------

class MedicalProductViewSet(viewsets.ModelViewSet):
    queryset = RefProduct.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MedicalProductListSerializer
        elif self.action == 'retrieve':
            return MedicalProductRetrieveSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return MedicalProductCreateSerializer if self.action == 'create' else MedicalProductUpdateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --------- ВЕТЕРИНАРНЫЕ АПТЕКИ -------------

class VetPharmacyViewSet(viewsets.ModelViewSet):
    queryset = RefShop.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return VetPharmacyListSerializer
        elif self.action == 'retrieve':
            return VetPharmacyRetrieveSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return VetPharmacyCreateSerializer if self.action == 'create' else VetPharmacyUpdateSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
