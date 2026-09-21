from django.urls import path
from rest_framework.decorators import api_view

from .views import (
    get_voitures,
    create_voiture,
    get_voiture_by_id,
    update_voiture,
    delete_voiture,
)


@api_view(["GET", "POST"])
def voitures_endpoint(request):
    if request.method == "GET":
        return get_voitures(request)

    return create_voiture(request)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def voiture_detail_endpoint(request, voiture_id):
    if request.method == "GET":
        return get_voiture_by_id(request, voiture_id)

    if request.method in ["PUT", "PATCH"]:
        return update_voiture(request, voiture_id)

    return delete_voiture(request)


urlpatterns = [
    path("", voitures_endpoint),
    path("<int:voiture_id>/", voiture_detail_endpoint),
]