from django.conf.urls import url, include
import payment.views
urlpatterns = [
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'signup/', payment.views.pay_view, name='signup-pay'),
    url(r'confirmed/', payment.views.confirmed, name="paypal-return"),
    url(r'canceled/', payment.views.canceled, name="paypal-cancel"),
]
