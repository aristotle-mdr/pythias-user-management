from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from pythias_user_management import views

urlpatterns = patterns(
    'pythias_user_management.views',
    url(r'^account/request_user/?$', views.request_new_user, name='request_new_user'),
    url(r'^', include('user_sessions.urls', 'user_sessions'))
)

