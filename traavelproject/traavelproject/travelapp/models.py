from django.db import models

# Create your models here.
class Comida(models.Model):
    nombre=models.CharField(max_length=250)
    precio=models.IntegerField()
    ingredientes=models.TextField()
    imagen=models.ImageField(upload_to='imagenes')

    def __str__(self):
        return self.nombre