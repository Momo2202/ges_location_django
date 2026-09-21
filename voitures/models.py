from django.db import models

from categories.models import Categorie

# Create your models here.
class Voiture(models.Model):
    marque=models.CharField(max_length=100)
    modele=models.CharField(max_length=100)
    immatriculation=models.CharField(max_length=50,unique=True)
    annee=models.PositiveIntegerField()
    prix_journalier=models.DecimalField(max_digits=10,decimal_places=2);
    disponible=models.BooleanField(default=True)
    categorie=models.ForeignKey(Categorie,on_delete=models.PROTECT,related_name="voitures")
    
    def __str__(self):
        return f"{self.marque} {self.modele}"
    
    