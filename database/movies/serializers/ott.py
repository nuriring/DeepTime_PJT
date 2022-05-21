from rest_framework import serializers
from ..models import Ott

class OttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ott
        fields = ('__all__')