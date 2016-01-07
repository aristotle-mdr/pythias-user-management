import autocomplete_light

from django import forms
from django.utils.translation import ugettext_lazy as _
from pythias_user_management.models import UserRequest
"""
"""
class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        exclude = ['date_requested','requested_by']