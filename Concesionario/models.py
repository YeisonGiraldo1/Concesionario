from django.db import models

class Auto(models.Model):
    Cilindraje = models.CharField(max_length=255)
    Matricula = models.CharField(max_length=255)
    Marca = models.CharField(max_length=255)
    Modelo = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    Cojineria = models.CharField(max_length=255)
    class Meta:
      db_table = 'auto'