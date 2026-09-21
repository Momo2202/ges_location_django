from .models import Voiture

def get_all_voitures(search=None):
    queryset=Voiture.objects.select_related("categorie").all()
    
    if search:
        queryset=queryset.filter(marque__icontains=search)
        
    return queryset


def find_voiture_by_id(voiture_id):
    return Voiture.objects.select_related("categorie").filter(id=voiture_id).first()

