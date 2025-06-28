from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Assistant
from .serializers import (
    AssistantListSerializer,
    AssistantRetrieveSerializer,
    AssistantCreateSerializer,
    AssistantUpdateSerializer,

)


class RefAssistantViewSet(viewsets.ModelViewSet):
    queryset = Assistant.objects.all()

    def get_queryset(self):
        queryset = Assistant.objects.all()

        # Фильтрация по статусу: ?is_done=true или false
        is_done = self.request.query_params.get('is_done')
        if is_done is not None:
            if is_done.lower() in ['true', '1']:
                queryset = queryset.filter(is_done=True)
            elif is_done.lower() in ['false', '0']:
                queryset = queryset.filter(is_done=False)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return AssistantListSerializer
        elif self.action == 'retrieve':
            return AssistantRetrieveSerializer
        elif self.action == 'create':
            return AssistantCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return AssistantUpdateSerializer

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
        serializer.save(users=request.user)  # автоматически связываем с текущим пользователем
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
