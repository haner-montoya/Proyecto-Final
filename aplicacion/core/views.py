from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'core/index.html'

    dict_context = {
        'title': 'Inicio',
        'message': 'Bienvenido a mi sitio web'
    }

    def get(self, request, *args, **kwargs):
        """Método que se encarga de devolver la vista"""
        return render(request, self.template_name, self.dict_context)
