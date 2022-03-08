from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):

    
    instanse = Product.objects.all().order_by('?').first()
    data = {}
    if instanse:
        data = ProductSerializer(instanse).data

    return Response(data)
    
 