from django.urls import path
from .views import (BuyItemView,
                    ItemListView,
                    ItemLandingPageView,
                    SuccessView,
                    CancelView,)

urlpatterns = [
    path('', ItemListView.as_view()),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<pk>/', ItemLandingPageView.as_view(), name='landing-page'),
    path('buy/<pk>/', BuyItemView.as_view(), name='buy-item')
]
