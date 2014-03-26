from django.conf.urls import patterns, include, url

from  .views import emotion_recorder_view, emotion_create_view

#from apps.auth.views import login_view

urlpatterns = patterns('',
    # Examples:
    url(r'^$', emotion_recorder_view, name="emotion_recorder"),
    url(r'^create$', emotion_create_view, name="emotion_create"),
)