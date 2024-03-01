from django.db import models

# Create your models here.

class Orden (models.Model):
    id = models.BigAutoField(primary_key=True)
    producto1 = models.CharField(max_length=50)
    producto2 = models.CharField(max_length=50)
    producto3 = models.CharField(max_length=50)
    producto4 = models.CharField(max_length=50)
