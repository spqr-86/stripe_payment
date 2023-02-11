from django.urls import path
from .views import OrderPageView, BuyOrderView

urlpatterns = [
    path('<pk>/', OrderPageView.as_view(), name='order'),
    path('buy/<pk>/', BuyOrderView.as_view(), name='buy-order')
]
