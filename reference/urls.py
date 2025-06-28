from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, ProductCategoryViewSet, BreedViewSet,
    AnimalSpeciesViewSet, MedicationViewSet, VetStoreViewSet
)

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'animal-species', AnimalSpeciesViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'vet-stores', VetStoreViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]