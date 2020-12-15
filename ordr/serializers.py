from rest_framework import serializers
from .models import Ordr


class OrdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordr
        fields = "__all__"
