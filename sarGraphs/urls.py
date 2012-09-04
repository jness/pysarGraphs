from django.conf.urls.defaults import patterns, include, url
from sarGraphs.views import HomeView, CpuView

urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home_view'),
)
