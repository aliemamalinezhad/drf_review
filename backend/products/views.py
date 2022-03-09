
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content = content)


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field  = 'pk'

# class ProductListAPIView(generic.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductListSerializer



