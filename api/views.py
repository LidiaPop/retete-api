from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Reteta, Meniu
from .serializers import RetetaSerializer, MeniuSerializer


class RetetaViewSet(ModelViewSet):
 queryset = Reteta.objects.all()
 serializer_class = RetetaSerializer
 permission_classes = [permissions.AllowAny]


class MeniuViewSet(ModelViewSet):
 queryset = Meniu.objects.all()
 serializer_class = MeniuSerializer
 permission_classes = [permissions.AllowAny]

