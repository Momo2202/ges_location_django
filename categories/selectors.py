from .models import Categorie

def get_all_categories(search=None):
    queryset=Categorie.objects.all()
    
    if search:
        queryset=queryset.filter(
            nom__icontains=search
        )
    return queryset


def find_categorie_by_id(categorie_id):
    return Categorie.objects.filter(id=categorie_id).first()