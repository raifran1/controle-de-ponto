from rest_framework.serializers import ModelSerializer, SerializerMethodField
from controle_de_ponto.models import Register 


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = ['rfid']
