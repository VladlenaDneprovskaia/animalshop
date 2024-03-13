from cart.service import Cart


def cart_processor(request):
    cart = Cart(request)
    return {
        'cart': {
            'items': cart.get_items(),
            'total_price': cart.get_total_price(),
            'total_count': cart.get_total_count(),
        }
    }
