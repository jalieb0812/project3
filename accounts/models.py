from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from orders.models import Menu_Item

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Menu_Item, blank=True)
    #stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        user_profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
