from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib import admin

admin.autodiscover()
dajaxice_autodiscover()


urlpatterns = patterns('',
    url(r'^posts/', include('posts.urls',namespace='posts')),
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

)

urlpatterns += staticfiles_urlpatterns()