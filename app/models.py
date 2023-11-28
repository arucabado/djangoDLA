from django.db import models
from django.contrib.auth.models import User    

# Create your models here.

class Miembro(models.Model):
    gametag = models.CharField(max_length=30, default=None)
    pais = models.CharField(max_length=30, default=None)
    zonah = models.CharField(max_length=30, default=None)
    horai = models.TimeField(default='00:00:00')
    duracion = models.IntegerField(default=0)
    mostrarnombre = models.BooleanField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        texto= "{0}"
        return texto.format(self.gametag)
    
    class Meta:
        db_table = 'Miembros'
