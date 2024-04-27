# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import CheckoutForm
from .models import Product


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect back to the product list page
    return redirect('product_list')  # Redirect in case of GET request or other cases


def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        Product.objects.create(name=product_name, price=product_price)
        return redirect('product_list')  # Redirect back to the product list page
    
    return redirect('product_list')  # Redirect in case of GET request or other cases

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
