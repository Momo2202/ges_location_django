from django.urls import path

from rest_framework.decorators import api_view

from .views import(
    get_clients,
    create_client,
    get_client_by_id,
    update_client,
    delete_client
)

@api_view(["GET","POST"])
def clients_endpoint(request):
    if request.method == "GET":
        return get_clients(request)
    
    return create_client(request)



@api_view(["GET","PUT","PATCH","DELETE"])
def client_detail_endpoint(request,client_id):
    if request.method=="GET":
        return get_client_by_id(request,client_id)
    
    if request.method in ["PUT","PATCH"]:
        return update_client(request,client_id)
    
    return delete_client(request,client_id)

urlpatterns = [
    path("",clients_endpoint),
    path("<int:client_id>/",client_detail_endpoint)
]
