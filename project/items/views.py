import stripe

from django.conf import settings
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.http import JsonResponse

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'


class ItemLandingPageView(DetailView):
    model = Item
    template_name = "items/item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item = Item.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(item.price) * 100,
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
