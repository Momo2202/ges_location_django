from rest_framework import serializers
from categories.models import Categorie
from categories.serializers import CategorieSerializer
from .models import Voiture


class VoitureSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(read_only=True)
    
    categorie_id=serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(),
        source="categorie",
        write_only=True
    )
    class Meta:
        model=Voiture
        fields=[
            "id",
            "marque",
            "modele",
            "immatriculation",
            "annee",
            "prix_journalier",
            "disponible",
            "categorie",
            "categorie_id"
        ]