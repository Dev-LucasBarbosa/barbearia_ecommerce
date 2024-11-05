from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from carts.models import Cart
from django.conf import settings
import stripe
import json

# Create your views here.
stripe.api_key = settings.STRIPE_API_KEY

def payment_success_view(request):
    return render(request, 'billing/payment-success.html')

def payment_failed_view(request):
    return render(request, 'billing/payment-failed.html')

def payment_method_view(request):
    context = {'publish_key': settings.STRIPE_PUB_KEY}
    return render(request, 'billing/payment-method.html', context)

@csrf_exempt
@require_POST
def create_payment_intent(request):
    data = json.loads(request.body)
    try:
        amount = calculate_order_amount(data['items'])

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='brl',
            payment_method_types=['card'],
        )
        return JsonResponse({'clientSecret': intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def calculate_order_amount(items):
    cart = Cart.objects.first()
    total_amount = 0
    for item in items:
        product = Product.objects.get(id=item['id'])
        total_amount += product.price * item['quantity']
    return int(total_amount * 100)