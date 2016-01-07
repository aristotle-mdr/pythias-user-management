from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from pythias_user_management.forms import NewUserForm

def request_new_user(request):
    context={}
    if request.method == 'POST':  # If the form has been submitted...
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            context.update({'success':True})
    else:
        form = NewUserForm()
        context.update({'blank':True})
    context.update({'form':form})
    return render(request,"pythias_user/request_user.html",context)
