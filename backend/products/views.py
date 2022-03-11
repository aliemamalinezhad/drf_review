from rest_framework import authentication, generics, mixins, permissions

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

from api.authentication import TokenAuthentication


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
        ]
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


product_list_view = ProductListCreateApiView.as_view()


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]



product_detail_view = ProductDetailApiView.as_view()


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# class CreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('title') or None
        if content is None:
            content = "this is my view doing every thing"
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()
