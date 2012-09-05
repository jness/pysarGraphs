from django.views.generic.base import TemplateView
from sarGraphs.lib.sar import get_cpu, get_load
from sarGraphs.lib.sar import get_swap, get_memory

class HomeView(TemplateView):
    'Home Page View'
   
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = {}
        context['cpu'] = get_cpu('%idle')
        context['iowait'] = get_cpu('%iowait')
        context['swap'] = get_swap('%swpused')
        context['mem'] = get_memory()
        context['load'] = get_load()
        return context 
