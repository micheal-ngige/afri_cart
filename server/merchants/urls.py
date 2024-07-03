from django.urls import path
from .views import MerchantListView, MerchantView, TopSellerView

urlpatterns = [
    path('', MerchantListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', MerchantView.as_view()),
]