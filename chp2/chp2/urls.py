from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from chp2.views import hello, hello_zeph

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chp2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', hello, name='hello'),
    url(r'^hello-zeph/$', hello_zeph, name='hello-zeph'),
    url(r'^admin/', include(admin.site.urls)),
)
