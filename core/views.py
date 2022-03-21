import logging

from django.views import generic

logging.basicConfig(level=logging.INFO)


class BaseIndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)

        return context
