from django.conf.urls import include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from gsd.views import timeline

urlpatterns = [
    url(r'^$', timeline, name='timeline'),
    url(r'^tasks/', include('todo.urls', app_name='todo', namespace='todo')),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain')),

    url(r'^admin/', include(admin.site.urls)),
]

