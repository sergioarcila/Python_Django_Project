from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@login_required
def pay_view(request):
    paypal_dict = {
      "cmd": "_xclick-subscriptions",
      "business": settings.PAYPAL_COMPANY_EMAIL,
      "a1": settings.PAYPAL_UPFRONT_COST,
      "p1": settings.PAYPAL_PERIOD[0],
      "t1": settings.PAYPAL_PERIOD[-1],

      "a3": settings.PAYPAL_RECURRENT_COST,
      "p3": settings.PAYPAL_PERIOD[0],                           # duration of each unit (depends on unit)
      "t3": settings.PAYPAL_PERIOD[-1],                         # duration unit ("M for Month")
      "src": "1",                        # make payments recur
      "sra": "1",                        # reattempt payment on payment error
      "no_note": "1",                    # remove extra notes (optional)
      "currency_code": "USD",
      "lc": "US",
      "item_name": "Be Scouted Now Annual Subscription",
      "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
      "return": request.build_absolute_uri(reverse('paypal-return')),
      "cancel_return": request.build_absolute_uri(reverse('paypal-cancel')),
      "custom": str(request.user.id),
    }


    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe')
    context = {"form": form}
    return render(request, "payment/payform.html", context)

@csrf_exempt
def confirmed(request):
  return render(request, "payment/payment-confirmed.html")

@csrf_exempt
def canceled(request):
  return render(request, "payment/payment-canceled.html")
