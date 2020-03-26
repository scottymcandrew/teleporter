from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """
    Renders the cart contents
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """
    Add specified feature to the cart
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('all_features'))


def adjust_cart(request, id):
    """
    Adjust the cart quantity
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, id):
    """
    Delete item from cart
    """
    cart = request.session.get('cart', {})
    print(cart)
    cart.pop(str(id))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
