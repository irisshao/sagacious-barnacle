from django.conf.urls import patterns, url
from aboutme_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^resume/$', views.resume, name='resume'),
	url(r'^connect/$', views.connect, name='connect'),
)