import stripe

from django.conf import settings
from django.views import View
from django.http import JsonResponse
from django.views.generic import DetailView

from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderPageView(DetailView):
    model = Order
    template_name = 'orders/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class BuyOrderView(View):
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs['pk'])
        domain = settings.BACKEND_DOMAIN
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item.price) * 100,
                        'product_data': {
                            'name': item.item.name,
                            'description': item.item.description,
                        },
                    },
                    'quantity': item.quantity,
                } for item in order.items.all()
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
