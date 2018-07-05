from django.conf.urls import url
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<i_id>[0-9]+)/$', views.detail),
]