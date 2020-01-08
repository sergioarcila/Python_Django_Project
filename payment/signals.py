from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from datetime import datetime
from django.conf import settings
from .models import SubscriptionStatus
from django.core.mail import send_mail

User = get_user_model() 

def notify(message, ipn_rx):
    printout = '\n '.join("%s: %s" % item for item in vars(ipn_rx).items())
    print(message+printout)
    send_mail("PAYPAL NOTIFICATION", message+printout, 'accounts@bescoutednow.com', ['efahnest@u.rochester.edu', 'tervin88@gmail.com'])

@receiver(valid_ipn_received)
def ipn_receiver(sender, **kwargs):
    ipn_obj = sender
    print(', '.join("%s: %s" % item for item in vars(ipn_obj).items()))

    if ipn_obj.txn_type == "subscr_signup":
        print("SUBSCRIPTION RECEIVED")

        payment_valid = True

        if ipn_obj.receiver_email != settings.PAYPAL_COMPANY_EMAIL:
            notify("emails did not match " + ipn_obj.receiver_email, ipn_obj)
            payment_valid = False
        if float(ipn_obj.amount1) != float(settings.PAYPAL_UPFRONT_COST):
            notify("upfront did not match: " + str(ipn_obj.amount1), ipn_obj)
            payment_valid = False
        if float(ipn_obj.amount3) != float(settings.PAYPAL_RECURRENT_COST):
            notify("recurrent did not match " + str(ipn_obj.amount3), ipn_obj)
            payment_valid = False
        if ipn_obj.period1 != settings.PAYPAL_PERIOD:
            notify("period 1 did not match " + ipn_obj.period1, ipn_obj)
            payment_valid = False
        if ipn_obj.period3 != settings.PAYPAL_PERIOD:
            notify("period 3 did not match " + ipn_obj.period3, ipn_obj)
            payment_valid = False
        if ipn_obj.currency_code != "USD":
            notify("Currency did not match " + ipn_obj.currency_code, ipn_obj)
            payment_valid = False

        if not payment_valid:
            print("Subsciption IPN deemed invalid")
            return

        # get user id and activate the account
        id = ipn_obj.custom
        try:
            user = User.objects.get(id=id)
        except:
            notify("Failed to get user with uuid " + id, ipn_obj)
            return
        try:
            sub_status = user.sub_status
        except: # if no substatus
            sub_status = SubscriptionStatus(user=user)
            

        sub_status.sub_id = ipn_obj.subscr_id
        sub_status.save()
 
 
    # check for subscription payment IPN
    elif ipn_obj.txn_type == "subscr_payment":
        print("SUBSCRIPTION PAYMENT RECEIVED")

        payment_valid = True
        # get user id and extend the subscription
        id = ipn_obj.custom
        user = None
        try:
            user = User.objects.get(id=id)
            
        except:
            notify("Failed to get user with uuid " + id, ipn_obj)
            return
        if user.sub_status.sub_id != ipn_obj.subscr_id:
            notify("Subscription ID did not match: " + user.sub_status.sub_id  + " and " + ipn_obj.subscr_id, ipn_obj)
            payment_valid = False
        if not (float(ipn_obj.mc_gross) == float(settings.PAYPAL_UPFRONT_COST) or float(ipn_obj.mc_gross) == float(settings.PAYPAL_RECURRENT_COST)):
            notify("Payment amount did not match: " + ipn_obj.mc_gross, ipn_obj)
            payment_valid = False

        if not payment_valid:
            print("Subsciption IPN deemed invalid")
            return

        user.sub_status.extend()
        print("Successfully extended subscription.")
        
 
 
    # check for failed subscription payment IPN
    if ipn_obj.txn_type == "subscr_failed":
        notify("Got a subscription failed\n", ipn_obj)
 
    # check for subscription cancellation IPN
    elif ipn_obj.txn_type == "subscr_cancel":
        notify("Got a subscription cancel", ipn_obj)

