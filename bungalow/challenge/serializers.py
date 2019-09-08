from rest_framework import serializers

from . import models


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Property
        fields = "__all__"  # ToDo: consider filtering fields
