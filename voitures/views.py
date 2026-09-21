from rest_framework import status
from rest_framework.response import Response

from .selectors import get_all_voitures, find_voiture_by_id
from .serializers import VoitureSerializer
from .services import (
    create_voiture_service,
    update_voiture_service,
    delete_voiture_service,
)

def get_voitures(request):
    search=request.query_params.get("search")
    voitures=get_all_voitures(search=search)
    serializer=VoitureSerializer(voitures,many=True)
    
    return Response(serializer.data)

def get_voiture_by_id(request,voiture_id):
    voiture=find_voiture_by_id(voiture_id)
    if voiture is None:
        return Response(
            {"detail":"Voiture Introuvable"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer=VoitureSerializer(voiture)
    return Response(serializer.data)

def create_voiture(request):
    serializer = VoitureSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    voiture = create_voiture_service(
        serializer.validated_data
    )

    return Response(
        VoitureSerializer(voiture).data,
        status=status.HTTP_201_CREATED,
    )

def update_voiture(request, voiture_id):
    voiture = find_voiture_by_id(voiture_id)

    if voiture is None:
        return Response(
            {"detail": "Voiture introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )

    partial = request.method == "PATCH"

    serializer = VoitureSerializer(
        voiture,
        data=request.data,
        partial=partial,
    )

    serializer.is_valid(raise_exception=True)

    voiture = update_voiture_service(
        voiture,
        serializer.validated_data
    )

    return Response(
        VoitureSerializer(voiture).data
    )


def delete_voiture(request, voiture_id):
    voiture = find_voiture_by_id(voiture_id)

    if voiture is None:
        return Response(
            {"detail": "Voiture introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )

    delete_voiture_service(voiture)

    return Response(
        status=status.HTTP_204_NO_CONTENT
    )