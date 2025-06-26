from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/pets/', views.pet_list, name='pet-list'),
    path('api/v1/pets/<int:pk>/', views.pet_detail, name='pet-detail'),
]
