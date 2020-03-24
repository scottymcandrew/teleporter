from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Makes cart contents available when rendering the page
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    feature_count = 0

    for id, quantity in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += quantity * feature.price
        feature_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'feature': feature})

    return {'cart_items': cart_items, 'total': total, 'feature_count': feature_count}
