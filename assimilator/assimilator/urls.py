from django.conf.urls import url
from django.contrib import admin

from . import sites

urlpatterns = [
    url(r'^parse/', sites.parse),
    url(r'', sites.home),
]
