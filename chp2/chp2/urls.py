from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from chp2.views import hello, hello_zeph, current_datetime, hours_ahead, intentional_error

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^hello/$', hello, name='hello'),
    url(r'^hello-zeph/$', hello_zeph, name='hello-zeph'),
    url(r'^clock/$', current_datetime, name='clock'),
	url(r'^time/plus/(\d+)/$', hours_ahead, name='time + x'),
    url(r'^boo/$', intentional_error, name='boo-hoo')
)
