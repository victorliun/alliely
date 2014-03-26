from django.conf.urls import patterns, include, url

from  apps.homepages.views import rose

#from apps.auth.views import login_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^I_LOVE_U$', rose, name="rose"),
    url(r'^er/', include("apps.emotion_recorder.urls")),
    url(r'^login/$', 'apps.auth.views.login_view', name='login'),
    url(r'^home/$', 'apps.homepages.views.rose', name='home'),
    )