from django.conf.urls import patterns, include, url
from .views import word_guess_view, dirtybot_view

urlpatterns = patterns('',
    #url(r'word_guess_view',)
    url(r'scraper/test$', dirtybot_view, name='scraper_view'),
)