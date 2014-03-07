from django.conf.urls import patterns, include, url

from  apps.homepages.views import rose

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rose$', rose, name="rose"),
    )