from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from clients.selectors import get_all_clients,find_client_by_id
from clients.serializers import ClientSerializer
from clients.services import create_client_service,update_client_service,delete_client_service

# Create your views here.

def get_clients(request):
    search=request.query_params.get("search")
    clients=get_all_clients(search=search)
    serializer=ClientSerializer(
        clients,
        many=True
    )
    
    return Response(serializer.data)
    

def get_client_by_id(request,client_id):
    client=find_client_by_id(client_id)
    
    if client is None:
        return Response(
            {"detail":"client introuvable"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer=ClientSerializer(client)
    return Response(serializer.data)


def create_client(request):
    serializer=ClientSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    client=create_client_service(serializer.validated_data)
    return Response(
        ClientSerializer(client).data,
        status=status.HTTP_201_CREATED,
    )
    
def update_client(request,client_id):
    client=find_client_by_id(client_id)
    
    if client is None:
        return Response(
            {"detail":"Client Introuvable"},
            status=status.HTTP_404_NOT_FOUND
        )
    partial=request.method=="PATCH"
    
    serializer=ClientSerializer(client,data=request.data,partial=partial)
    
    serializer.is_valid(raise_exception=True)
    
    client=update_client_service(client,serializer.validated_data)
    
    return Response(ClientSerializer(client).data)


def delete_client(request,client_id):
    client=find_client_by_id(client_id)
    if client is None:
        return Response(
            {"detail":"Client Introuvable"},
            status=status.HTTP_404_NOT_FOUND
        )
    delete_client_service(client)
    
    return Response(
        status=status.HTTP_204_NO_CONTENT
    )