from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from chp2.views import hello, hello_zeph, current_datetime, hours_ahead, intentional_error
from chp2.views import current_datetime_template, current_datetime_template_file, current_datetime_template_shortcut
from chp2.views import handle_vanilla_template, request_viewer

urlpatterns = patterns('',
    url(r'^__request__.*/$', request_viewer, name='request viewer'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^hello/$', hello, name='hello'),
    url(r'^hello-zeph/$', hello_zeph, name='hello-zeph'),
    url(r'^clock/$', current_datetime, name='clock'),
    url(r'^clock2/$', current_datetime_template, name='clock2'),
    url(r'^clock3/$', current_datetime_template_file, name='clock3'),
    url(r'^clock4/$', current_datetime_template_shortcut, name='clock4'),
    url(r'^time/plus/(\d+)/$', hours_ahead, name='time + x'),
    url(r'^boo/$', intentional_error, name='boo-hoo'),
 	url(r'^(.+[.]html)/(.*)$', handle_vanilla_template, name='generic template'),       
)
