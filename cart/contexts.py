from django.conf import settings
from django.shortcuts import get_object_or_404
from meals.models import Meal


def cart_contents(request):

    cart_items = []
    total = 0
    meal_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        meal = get_object_or_404(Meal, pk=item_id)
        total += quantity * meal.price
        meal_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'meal': meal,
        })

    ''' Display delivery cost only if total is greater 0 '''
    if total > 0:
        delivery = 39
    else:
        delivery = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'meal_count': meal_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
