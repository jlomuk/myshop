from django.shortcuts import render, redirect 
from django.utils import timezone 
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import CouponApplyForm
from cart.cart import Cart

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data.get('code')
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id 
        except:
            if not request.session.get('coupon_id'):
                request.session['coupon_id'] = None 
    return redirect('cart:cart_detail')


@require_POST
def coupon_delete(request):
    cart = Cart(request)
    cart.delete_coupon()
    return redirect('cart:cart_detail')
