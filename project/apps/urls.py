from django.conf.urls import patterns, include, url

from  apps.homepages.views import rose
from  apps.emotion_recorder.views import emotion_recorder_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rose$', rose, name="rose"),
    url(r'^er$', emotion_recorder_view, name="emotion_recorder_view"),
    )