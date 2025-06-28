from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RefAssistantViewSet

router = DefaultRouter()
router.register(r'reminder', RefAssistantViewSet, basename='reminder')

urlpatterns = router.urls
