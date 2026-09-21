from .models import Categorie

def create_categorie_service(validated_data):
    return Categorie.objects.create(**validated_data)

def update_categorie_service(categorie,validated_data):
    for field, value in validated_data.items():
        setattr(categorie,field,value)
    
    categorie.save()
    return categorie

def delete_categorie_service(categorie):
    categorie.delete()