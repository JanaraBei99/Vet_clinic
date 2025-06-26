from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Pet
from .serializers import PetSerializer


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

@api_view(['GET', 'POST'])
def pet_list(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE', 'HEAD'])
def pet_detail(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET' or request.method == 'HEAD':
        serializer = PetSerializer(pet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pet.delete()
        return Response(status=204)

