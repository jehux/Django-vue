from django.db import models

# Create your models here.



class Moneda(models.Model):
    dolar = models.FloatField()
    fecha = models.DateField()
    
class UDI(models.Model):
    udi = models.FloatField()
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    def __str__(self):
        return self.tipo