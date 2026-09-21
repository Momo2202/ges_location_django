from django.urls import path
from rest_framework.decorators import api_view

from .views import(
    get_categories,
    create_categorie,
    get_categorie_by_id,
    update_categorie,
    delete_categorie
)

@api_view(["GET","POST"])
def categories_endpoint(request):
    if request.method == "GET":
        return get_categories(request)
    
    return create_categorie(request)

@api_view(["GET","PUT","PATCH","DELETE"])
def categorie_detail_endpoint(request,categorie_id):
    if request.method=="GET":
        return get_categorie_by_id(request,categorie_id)
    
    if request.method in["PUT","PATCH"]:
        return update_categorie(request,categorie_id)
    
    return delete_categorie(request,categorie_id)


urlpatterns = [
    path("",categories_endpoint),
    path("<int:categorie_id>/",categorie_detail_endpoint)
]
