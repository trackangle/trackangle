from django.conf.urls import url
from trackangle.route.views import BaseRouteView

urls = [
    url(r'^create/$', BaseRouteView.as_view(), name='create'),
]