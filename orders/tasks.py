from myshop.celery import app

from django.conf import settings
from django.core.mail import send_mail

from .models import Order 


@app.task()
def order_created(order_id):
    if not settings.DEBUG:
        order = Order.objects.get(id=order_id)
        subject = f"Order № {order.id}"
        message = f'Dear {order.first_name},\n\nYou have successfully placed an order.You order id is {order.id}'
        mail_send = send_mail(subject, message, 'admin@myshop.com', [order.email], fail_silently=True)
        return mail_send