from django.db import models

# Create your models here.
class Client(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    telephone=models.CharField(max_length=30)
    adresse=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"