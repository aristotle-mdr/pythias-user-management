from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from aristotle_mdr.utils import url_slugify_concept

def test(request):
     return render(request,"pythias_user/tests.html",{})
