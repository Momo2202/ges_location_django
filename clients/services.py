from .models import Client

def create_client_service(validated_data):
    return Client.objects.create(**validated_data)

def update_client_service(client,validated_data):
    for field,value in validated_data.items():
        setattr(client,field,value)
    
    client.save()
    return client

def delete_client_service(client):
    client.delete()