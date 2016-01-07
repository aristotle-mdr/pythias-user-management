from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

from aristotle_mdr import models as MDR

#@receiver(post_save,sender=MDR._concept)
#@receiver(post_save)
#def do_thing_with_concepts(sender, instance, created, **kwargs):
#    if not issubclass(sender, MDR._concept):
#        return

class UserRequest(models.Model):
    username = models.CharField(
        help_text = _('The requested username for a new account'),
        blank=True,
        null=True,
        max_length=256
    )
    email = models.EmailField(
        help_text = _('A valid email address used for contact and follow up'),
    )
    contact_name =  models.CharField(
        help_text = _('The name of the person requesting the account'),
        max_length=1024
    )
    account_name =  models.CharField(
        help_text = _('The name of the person the account account will be for'
                        'Leave blank if this is also the contact person.'),
        blank=True,
        null=True,
        max_length=1024
    )
    other_contact_details =  models.TextField(
        help_text = _('Other contact details or information to '
                        'support the request'),
        blank=True,
        null=True
    )
    date_requested = models.DateTimeField(
        help_text = _('The date and time an account was requested'),
        auto_now_add=True
    )
    requested_by = models.ForeignKey(
        User,
        help_text = _('An active user who was associated with this request'),
        blank=True,
        null=True,
        related_name="requested_users"
    )