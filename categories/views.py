from rest_framework import status
from rest_framework.response import Response

from .selectors import get_all_categories, find_categorie_by_id
from .serializers import CategorieSerializer
from .services import (
    create_categorie_service,
    update_categorie_service,
    delete_categorie_service,
)


def get_categories(request):
    search = request.query_params.get("search")

    categories = get_all_categories(search=search)

    serializer = CategorieSerializer(
        categories,
        many=True
    )

    return Response(serializer.data)


def get_categorie_by_id(request, categorie_id):
    categorie = find_categorie_by_id(categorie_id)

    if categorie is None:
        return Response(
            {"detail": "Catégorie introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = CategorieSerializer(categorie)

    return Response(serializer.data)


def create_categorie(request):
    serializer = CategorieSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    categorie = create_categorie_service(
        serializer.validated_data
    )

    return Response(
        CategorieSerializer(categorie).data,
        status=status.HTTP_201_CREATED,
    )


def update_categorie(request, categorie_id):
    categorie = find_categorie_by_id(categorie_id)

    if categorie is None:
        return Response(
            {"detail": "Catégorie introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )

    partial = request.method == "PATCH"

    serializer = CategorieSerializer(
        categorie,
        data=request.data,
        partial=partial,
    )

    serializer.is_valid(raise_exception=True)

    categorie = update_categorie_service(
        categorie,
        serializer.validated_data,
    )

    return Response(
        CategorieSerializer(categorie).data
    )


def delete_categorie(request, categorie_id):
    categorie = find_categorie_by_id(categorie_id)

    if categorie is None:
        return Response(
            {"detail": "Catégorie introuvable."},
            status=status.HTTP_404_NOT_FOUND,
        )

    delete_categorie_service(categorie)

    return Response(
        status=status.HTTP_204_NO_CONTENT
    )