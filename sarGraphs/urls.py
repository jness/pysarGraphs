from django.conf.urls.defaults import patterns, include, url
from sarGraphs.views import HomeView

urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home_view'),
)
