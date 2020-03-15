from rest_framework import serializers
from .models import NatParks


class NatParksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description',
            'picture',
            'location',
        )
        model = NatParks
