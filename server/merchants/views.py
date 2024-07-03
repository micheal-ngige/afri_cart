from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Merchant
from .serializers import MerchantSerializer

class MerchantListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    pagination_class = None

class MerchantView(RetrieveAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Merchant.objects.filter(top_seller=True)
    serializer_class = MerchantSerializer
    pagination_class = None