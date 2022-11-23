from django.db import models

# Create your models here.

class item(models.Model):
    nomb = models.CharField(max_length=30)
    descrip=models.CharField(max_length=200)
    talla=models.CharField(max_length=3)
    valor=models.IntegerField()
    cant=models.IntegerField()
    tipo = models.CharField(max_length=30)
    imagen=models.ImageField(upload_to="productos",null=True)

class compra(models.Model):
    num_comp = models.IntegerField()
    nom_cli = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    id_prod = models.ForeignKey(item, on_delete=models.CASCADE)
    descrip=models.CharField(max_length=200, null=True)
    fecha=models.DateTimeField(auto_now_add=True)
    cantidad=models.SmallIntegerField()
    valorcomp=models.IntegerField()
