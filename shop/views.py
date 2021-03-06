from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    language = request.LANGUAGE_CODE
    if category_slug:
        category = get_object_or_404(Category, translations__language_code=language, 
                                                translations__slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, id=id, 
                                translations__language_code=language, 
                                translations__slug=slug, 
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 
                'shop/product/detail.html', 
                {'product': product, 'cart_product_form': cart_product_form})