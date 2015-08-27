from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aboutme_project.views.home', name='home'),
    # url(r'^aboutme_project/', include('aboutme_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'', include('aboutme_app.urls')),
    url(r'^aboutme_app/', include('aboutme_app.urls')), # Adding new tuple
)
