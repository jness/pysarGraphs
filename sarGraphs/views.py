from django.views.generic.base import TemplateView
from sarGraphs.lib.sar import get_cpu

class HomeView(TemplateView):
    'Home Page View'
   
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = {}
        r = get_cpu('idle')
        context['data'] = r
        return context 
