from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    RoleViewSet,
    ProductCategoryViewSet,
    BreedViewSet,
    AnimalTypeViewSet,
    MedicalProductViewSet,
    VetPharmacyViewSet
)

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'categories', ProductCategoryViewSet, basename='category')
router.register(r'breeds', BreedViewSet, basename='breed')
router.register(r'animal-types', AnimalTypeViewSet, basename='animaltype')
router.register(r'medical-products', MedicalProductViewSet, basename='medicalproduct')
router.register(r'vet-pharmacies', VetPharmacyViewSet, basename='vetpharmacy')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
