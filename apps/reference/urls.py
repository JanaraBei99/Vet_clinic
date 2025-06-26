from rest_framework import routers
from .views import (
    RefShopViewSet,
    RefProductCategoryViewSet,
    RefBreedViewSet,
    RefRoleViewSet,
    RefTypeOfAnimalViewSet,
    RefProductViewSet,
)

router = routers.DefaultRouter()

router.register(r'ref_shops', RefShopViewSet)
router.register(r'ref_product_category', RefProductCategoryViewSet)
router.register(r'ref_breeds', RefBreedViewSet)
router.register(r'ref_roles', RefRoleViewSet)
router.register(r'ref_type_of_animal', RefTypeOfAnimalViewSet)
router.register(r'ref_products', RefProductViewSet)

urlpatterns = router.urls