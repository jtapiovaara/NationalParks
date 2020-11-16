from django.views import generic
from rest_framework import generics

from NationalParks.settings import NASA_API_KEY
from .models import NatParks, NatParkGeo
from .serializers import NatParksSerializer


class ListNatParks(generics.ListCreateAPIView):
    queryset = NatParks.objects.all()
    serializer_class = NatParksSerializer


class DetailNatParks(generics.RetrieveUpdateDestroyAPIView):
    queryset = NatParks.objects.all()
    serializer_class = NatParksSerializer


class PicNatParks(generic.ListView):
    model = NatParks

    # def nasakey(self):
    #     nasakey = NASA_API_KEY
    #     return nasakey

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nasakey'] = NASA_API_KEY
        return context


