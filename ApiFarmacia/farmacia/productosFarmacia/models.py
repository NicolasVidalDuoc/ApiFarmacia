from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=60)
    stock_producto = models.IntegerField()

    def __str__(self):
        return self.nombre_producto


#Hola Josao Cofrao
#Seba Entero Feo