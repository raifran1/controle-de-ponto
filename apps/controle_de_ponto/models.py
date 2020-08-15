from django.db import models

# Create your models here.

class RegisterManager(models.Manager):
    def search(self, search):
        print(search)
        return self.get_queryset().filter(**search)

class Register(models.Model):

    TIPO = [
        ('EN','Entrada'),
        ('SA','Saída'),
    ]

    rfid = models.CharField(max_length=40)
    data = models.DateField(auto_now_add=False)
    horario_entrada = models.TimeField('Horário entrada', auto_now=False, auto_now_add=False, blank=True, null=True)
    horario_saida = models.TimeField('Horário saída', auto_now=False, auto_now_add=False, blank=True, null=True)
    servico = models.TextField(blank=True)

    objects = models.Manager()
    registros = RegisterManager()