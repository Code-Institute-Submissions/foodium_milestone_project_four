from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    meal_count = 0
    delivery = 39
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'meal_count': meal_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
