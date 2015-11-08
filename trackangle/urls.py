from django.conf.urls import include, url, patterns
from django.contrib import admin

from .route.urls import urls as route_urls
from .dashboard.urls import urls as dashboard_urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include(dashboard_urls, namespace='dashboard')),
    url(r'^route/', include(route_urls, namespace='route')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

)