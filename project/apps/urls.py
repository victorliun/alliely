from django.conf.urls import patterns, include, url

from  apps.homepages.views import site_home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', site_home, name="site_home"),
    )