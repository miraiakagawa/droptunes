from django.conf.urls import patterns, include, url
from droptunes.views import hello_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', view=hello_view, name='hello_view'),
    # Examples:
    # url(r'^$', 'droptunes_project.views.home', name='home'),
    # url(r'^droptunes_project/', include('droptunes_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
	urlpatterns += patterns(”,
	(r’^static/(?P.*)$’, ‘django.views.static.serve’, {‘document_root’: settings.STATIC_ROOT}),
	)