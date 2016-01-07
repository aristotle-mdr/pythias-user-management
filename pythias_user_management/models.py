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
