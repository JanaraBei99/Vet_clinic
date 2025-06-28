from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import RefShop, RefProductCategory, RefBreed, RefRole, RefTypeOfAnimal, RefProduct
from .serializers import (
    RefRoleSerializer,
    RefProductCategorySerializer,
    RefBreedSerializer,
    RefShopSerializer,
    RefTypeOfAnimalSerializer,
    RefProductSerializer,
)


class RefShopViewSet(viewsets.ModelViewSet):
    queryset = RefShop.objects.all()
    serializer_class = RefShopSerializer


class RefProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = RefProductCategory.objects.all()
    serializer_class = RefProductCategorySerializer


class RefBreedViewSet(viewsets.ModelViewSet):
    queryset = RefBreed.objects.all()
    serializer_class = RefBreedSerializer


class RefRoleViewSet(viewsets.ModelViewSet):
    queryset = RefRole.objects.all()
    serializer_class = RefRoleSerializer


class RefTypeOfAnimalViewSet(viewsets.ModelViewSet):
    queryset = RefTypeOfAnimal.objects.all()
    serializer_class = RefTypeOfAnimalSerializer


class RefProductViewSet(viewsets.ModelViewSet):
    queryset = RefProduct.objects.all()
    serializer_class = RefProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('search', None)
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset