from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import ShoeSerializer, ShoeColorSerializer, ManufacturerSerializer, ShoeTypeSerializer
from api.models import Shoe, ShoeColor, ShoeType, Manufacturer
# Create your views here.

# Joe actually learned coding from the original programmers growing up in the Savanna, the Hyenas


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
