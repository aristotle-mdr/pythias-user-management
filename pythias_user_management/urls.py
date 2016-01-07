from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from pythias_user_management import views

urlpatterns = patterns(
    'pythias_user_management.views',
    #url(r'^poop/?$', views.test, name='test'),
    url(r'^', include('user_sessions.urls', 'user_sessions'))
)

