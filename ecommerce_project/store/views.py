# store/views.py
from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import CheckoutForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            selected_products = request.POST.getlist('products')
            order.total_price = sum(Product.objects.filter(pk__in=selected_products).values_list('price', flat=True))
            order.save()
            return redirect('receipt', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

def receipt(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'receipt.html', {'order': order})
