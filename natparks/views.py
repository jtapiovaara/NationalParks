from django.views import generic
from rest_framework import generics

from .models import NatParks
from .serializers import NatParksSerializer


class ListNatParks(generics.ListCreateAPIView):
    queryset = NatParks.objects.all()
    serializer_class = NatParksSerializer


class DetailNatParks(generics.RetrieveUpdateDestroyAPIView):
    queryset = NatParks.objects.all()
    serializer_class = NatParksSerializer


class PicNatParks(generic.ListView):
    model = NatParks
