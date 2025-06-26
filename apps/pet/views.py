from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pet
from .serializers import (
    PetListSerializer,
    PetRetrieveSerializer,
    PetCreateSerializer,
    PetUpdateSerializer
)

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()


    def get_serializer_class(self):
        if self.action == 'list':
            return PetListSerializer
        elif self.action == 'retrieve':
            return PetRetrieveSerializer
        elif self.action == 'create':
            return PetCreateSerializer
        elif self.action == 'update':
            return PetUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)  # partial=False для PUT
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




# class PetViewSet(viewsets.ModelViewSet):
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializer
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return PetListSerializer
#         elif self.action == 'retrieve':
#             return PetRetrieveSerializer
#         elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
#             return PetCreateChangeSerializer
#
#     def post(self, request, *args, **kwargs):
#         pass
#     def list(self, request, *args, **kwargs):
#         pass
#     def retrieve(self, request, *args, **kwargs):
#         pass

