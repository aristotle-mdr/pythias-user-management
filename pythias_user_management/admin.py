from django.contrib import admin
from pythias_user_management import models

class UserRequestAdmin(admin.ModelAdmin):
    model = models.UserRequest
    list_display = ['username', 'email', 'contact_name', 'date_requested']
    list_filter = ['email', 'requested_by']

admin.site.register(models.UserRequest,UserRequestAdmin)
