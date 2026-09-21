from .models import Voiture

def create_voiture_service(validate_data):
    return Voiture.objects.create(**validate_data)


def update_voiture_service(voiture,validate_data):
    for field,value in validate_data.items():
        setattr(voiture,field,value)
    
    voiture.save()
    return voiture


def delete_voiture_service(voiture):
    voiture.delete()