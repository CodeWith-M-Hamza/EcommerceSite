from django.shortcuts import render,get_object_or_404,redirect
from .models import Order, OrderItem
from cart.models import Cart, CartItem

from .forms import OrderCreateForm



def order_create(request):
    cart=None
    cart_id=request.session.get('cart_id')
    if cart_id:
        cart=get_object_or_404(Cart,id=cart_id)
        if not cart or not cart.items.exists():
            return redirect('cart:cart_detail')
    if request.method == 'POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.paid=False
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            cart.delete()
            del request.session['cart_id']
            return redirect('orders:order_confirmation', order_id=order.id)
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order_create.html', {'form': form, 'cart': cart})
def order_confirmation(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})