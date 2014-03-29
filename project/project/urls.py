from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()

from apps.auth.views import logout_view


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("apps.urls")),
    url(r'accounts/login/$', login, name="login"),
    url(r'accounts/logout/$', logout_view, name="logout"),
    #url(r'^', include('cms.urls')),
)

urlpatterns += patterns('',
	(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)