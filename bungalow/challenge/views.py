from rest_framework import viewsets

from . import models
from . import serializers


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Property.objects.all()  # ToDo: Order queryset
    serializer_class = serializers.PropertySerializer
