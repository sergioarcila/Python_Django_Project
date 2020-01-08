from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
from paypal.standard import models as pp_models

def return_future():
  a = timezone.now()
  return a + timezone.timedelta(hours=1)

class SubscriptionStatus(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='sub_status')

  date_created = models.DateTimeField("Date Created", default=timezone.now)
  date_updated = models.DateTimeField("Date Updated", default=timezone.now)

  # status = models.BooleanField("Subscription Status", default=False)

  sub_id = models.CharField("Subscription ID", max_length=100, blank=True)

  expiration = models.DateTimeField("Subscription Expiration", default=return_future)

  def status(self):
    return timezone.now() < self.expiration
  
  def extend(self):
    # set to end of day, just to make sure subscriptions have time to get through
    self.expiration = timezone.now() + timezone.timedelta(days=366)
    self.expiration = self.expiration.replace(hour=23,minute=59)
    self.save()
    
  def __str__(self):
    # if self.user is not None:
    try:
      return self.user.email + " " + str(self.expiration)
    except:
      return "No user " + str(self.expiration)