from django.shortcuts import render,get_object_or_404,redirect
from products.models import Product
from .models import Cart,CartItem
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# Create your views here.


@require_POST
def cart_add(request,product_id):
    cart_id=request.session.get('cart_id')
    if cart_id:
        try:
            cart=Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart=Cart.objects.create()
    else:
        cart=Cart.objects.create()
        request.session['cart_id']=cart.id
    products=get_object_or_404(Product,id=product_id)
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=products)
    if not created:
        cart_item.quantity+=1
    cart_item.save()
    response_data={
        'success':True,
        'message':f"{products.name} added to cart successfully.",


    }
    return JsonResponse(response_data)
def cart_detail(request):
    cart_id=request.session.get('cart_id')
    cart=None
    if cart_id:
        cart=get_object_or_404(Cart,id=cart_id)
    return render(request,'cart/detail.html',{'cart':cart})

  # or your product model


from django.http import JsonResponse, Http404
from .models import Cart, CartItem, Product

def cart_remove(request, product_id):
    if request.method == 'POST':
        cart_id = request.session.get('cart_id')
        if not cart_id:
            return JsonResponse({'success': False, 'message': 'Cart not found'})

        try:
            cart = Cart.objects.get(id=cart_id)
            product = Product.objects.get(id=product_id)
            cart_item = CartItem.objects.get(cart=cart, product=product)
        except (Cart.DoesNotExist, Product.DoesNotExist, CartItem.DoesNotExist):
            return JsonResponse({'success': False, 'message': 'Item not found'})

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            quantity_left = cart_item.quantity
        else:
            cart_item.delete()
            quantity_left = 0

        return JsonResponse({
            'success': True,
            'message': f'{product.name} removed from cart.',
            'quantity_left': quantity_left,
            'product_id': product.id,
        })

    return JsonResponse({'success': False, 'message': 'Invalid request'})


# def cart_remove(request, product_id):
#     cart_id = request.session.get('cart_id')
#     cart = get_object_or_404(Cart, id=cart_id)
#     cart_item = get_object_or_404(CartItem, cart=cart, product__id=product_id)

#     cart_item.delete()
#     return redirect('cart:cart_detail')