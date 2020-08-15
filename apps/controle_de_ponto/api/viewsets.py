from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterSerializer
from ..models import Register 
from datetime import datetime
from rest_framework.response import Response

class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

    def create(self, validated_data):
        tag = self.request.data['rfid']
        try:
            registro = Register.objects.get(rfid=tag, horario_saida=None)
            registro.horario_saida = datetime.now().strftime("%H:%M:%S")
            registro.data = datetime.now().today()
            registro.save()
            return Response({'POST':'Saída registrada'})
        except:
            registro = Register(
                rfid=tag,
                horario_entrada=datetime.now().strftime("%H:%M:%S"),
                data=datetime.now().today()
            )
            registro.save()
            return Response({'POST':'Entrada registrada'})
