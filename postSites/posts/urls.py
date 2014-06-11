from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^viewPosts/$', views.listing, name='viewPosts'),
	url(r'^viewComments/$', views.viewComments, name='viewComments'),
	url(r'^(?P<post_id>\d+)/viewComments/$', views.viewComments, name='viewComments'),

)

