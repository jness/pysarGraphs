from django.views.generic.base import TemplateView
from sarGraphs.lib.sar import get_cpu, get_load

class HomeView(TemplateView):
    'Home Page View'
   
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = {}
        context['cpu'] = get_cpu('%idle')
        context['load'] = get_load('ldavg-5')
        return context 
