from django.conf.urls import patterns, include, url
from django.contrib import admin

from dis2_backend.api.api import api_patterns
import django_project.settings as settings

admin.autodiscover()



urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(api_patterns)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)



