from rest_framework.serializers import ModelSerializer
from .models import ProgrmmingCard

class ProgrammingCardSerializer(ModelSerializer):
    class Meta:
        model = ProgrmmingCard
        fields = '__all__'