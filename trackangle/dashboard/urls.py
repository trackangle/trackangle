from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import BaseDashboardView

urls = [
    url(r'^$', login_required(BaseDashboardView.as_view(), login_url='/accounts/login'), name='hde'),
]