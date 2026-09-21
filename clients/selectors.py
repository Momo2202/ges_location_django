from .models import Client

def get_all_clients(search=None):
    queryset=Client.objects.all()
    
    if search:
        queryset=queryset.filter(
            nom_icontains=search
        )
    
    return queryset


def find_client_by_id(client_id):
    return Client.objects.filter(id=client_id).first()